# -*- coding: utf-8 -*-
"""Empacota a skill para upload no claude.ai.

    python empacotar.py

Gera em dist/:
    precificar-enterprise.zip                    <- o que sobe no claude.ai
    COMO-INSTALAR-precificar-enterprise.md       <- o README, para ler sem descompactar

Os .md da raiz deste repositorio sao a unica fonte da verdade. O zip e copia fiel deles:
nao edite nada dentro de dist/, edite aqui e rode isto de novo.
"""
import re
import shutil
import sys
import zipfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
ORIGEM = RAIZ
NOME_SKILL = "precificar-enterprise"      # tem de bater com o `name:` do SKILL.md
DIST = RAIZ / "dist"
STAGE = DIST / NOME_SKILL

erros = []


def falha(msg):
    erros.append(msg)


def ler_frontmatter(texto):
    if not texto.startswith("---\n"):
        falha("SKILL.md nao comeca com frontmatter YAML (`---`)")
        return {}
    fim = texto.find("\n---\n", 3)
    if fim == -1:
        falha("frontmatter do SKILL.md nao fecha com `---`")
        return {}
    campos = {}
    for linha in texto[4:fim].split("\n"):
        if not linha.strip():
            continue
        if ":" not in linha:
            falha("linha de frontmatter sem `chave: valor`: %r" % linha)
            continue
        chave, valor = linha.split(":", 1)
        campos[chave.strip()] = valor.strip()
    return campos


def validar():
    """As regras do claude.ai. Falhar aqui e mais barato que falhar no upload."""
    if not ORIGEM.is_dir():
        falha("pasta de origem nao existe: %s" % ORIGEM)
        return

    skill_md = ORIGEM / "SKILL.md"
    if not skill_md.is_file():
        falha("SKILL.md nao existe em %s" % ORIGEM)
        return

    texto = skill_md.read_text(encoding="utf-8")
    fm = ler_frontmatter(texto)

    nome = fm.get("name", "")
    if not nome:
        falha("frontmatter sem `name`")
    else:
        if nome != NOME_SKILL:
            falha("`name: %s` difere da pasta do zip (%s) — o claude.ai quer os dois iguais"
                  % (nome, NOME_SKILL))
        if len(nome) > 64:
            falha("`name` tem %d caracteres (maximo 64)" % len(nome))
        if not re.fullmatch(r"[a-z0-9-]+", nome):
            falha("`name` so aceita minusculas, numeros e hifen: %r" % nome)
        for reservada in ("claude", "anthropic"):
            if reservada in nome.lower():
                falha("`name` contem a palavra reservada %r" % reservada)

    desc = fm.get("description", "")
    if not desc:
        falha("frontmatter sem `description` — e o que faz a skill ser encontrada")
    elif len(desc) > 1024:
        falha("`description` tem %d caracteres (maximo 1024)" % len(desc))
    if "<" in desc or ">" in desc:
        falha("`description` nao pode conter tag XML")

    # allowed-tools nao existe no claude.ai; deixar la nao quebra, mas engana quem le
    if "allowed-tools" in fm:
        falha("frontmatter tem `allowed-tools`, que o claude.ai ignora — remova")

    # todo link relativo tem de apontar para arquivo que vai no zip
    for md in sorted(ORIGEM.glob("*.md")):
        for alvo in re.findall(r"\]\(([^)]+)\)", md.read_text(encoding="utf-8")):
            if alvo.startswith(("http://", "https://", "#", "mailto:")):
                continue
            if not (ORIGEM / alvo.split("#")[0]).exists():
                falha("%s aponta para `%s`, que nao existe na skill" % (md.name, alvo))


def empacotar():
    if DIST.exists():
        shutil.rmtree(DIST)
    STAGE.mkdir(parents=True)

    # so o material da skill: fora dotfiles (.gitignore) e scripts (.py)
    arquivos = sorted(p for p in ORIGEM.iterdir()
                      if p.is_file() and not p.name.startswith(".") and p.suffix != ".py")

    # a pasta de origem e CRLF (Windows); o zip sai em LF, que qualquer plataforma le igual
    texto = {".md", ".csv", ".txt", ".json", ".yaml", ".yml", ".py"}
    for arq in arquivos:
        if arq.suffix.lower() in texto:
            (STAGE / arq.name).write_bytes(arq.read_bytes().replace(b"\r\n", b"\n"))
        else:
            shutil.copy2(arq, STAGE / arq.name)

    zip_path = DIST / ("%s.zip" % NOME_SKILL)
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for arq in arquivos:
            z.write(STAGE / arq.name, "%s/%s" % (NOME_SKILL, arq.name))

    shutil.copy2(STAGE / "README.md", DIST / ("COMO-INSTALAR-%s.md" % NOME_SKILL))

    return zip_path, arquivos


if __name__ == "__main__":
    validar()
    if erros:
        print("nao empacotei — %d problema(s):" % len(erros))
        for e in erros:
            print("  x %s" % e)
        sys.exit(1)

    zip_path, arquivos = empacotar()
    print("ok — %s (%.1f KB, %d arquivos)"
          % (zip_path.name, zip_path.stat().st_size / 1024, len(arquivos)))
    for arq in arquivos:
        print("   %s/%s" % (NOME_SKILL, arq.name))
    print("\nsobe esse .zip em Settings > Features > Skills, no claude.ai.")
