#!/usr/bin/env python3
"""
Gupy Match Analyzer
Analisa o alinhamento entre um perfil de candidato e um job description da Gupy.
Uso: python gupy_match_analyzer.py
"""

import re
import sys
from typing import Optional


def extract_keywords(text: str) -> list[str]:
    """Extrai palavras-chave relevantes de um texto."""
    # Remover pontuação e converter para minúsculas
    text_lower = text.lower()
    # Padrões comuns em job descriptions
    tech_patterns = [
        r'\bpython\b', r'\bjava\b', r'\bjavascript\b', r'\btypescript\b',
        r'\bsql\b', r'\bexcel\b', r'\bpower bi\b', r'\btableau\b',
        r'\bscrum\b', r'\bagile\b', r'\bkanban\b', r'\bjira\b',
        r'\bsalesforce\b', r'\bsap\b', r'\baws\b', r'\bazure\b',
        r'\bgcp\b', r'\bdocker\b', r'\bkubernetes\b', r'\bgit\b',
        r'\breact\b', r'\bnode\.?js\b', r'\bdjango\b', r'\bflask\b',
    ]
    soft_patterns = [
        r'\bliderança\b', r'\bcomunicação\b', r'\bproatividade\b',
        r'\bgestão\b', r'\banalítico\b', r'\bequipe\b', r'\bcolaboração\b',
        r'\borganização\b', r'\bplanejamento\b', r'\bnegociação\b',
    ]
    found = []
    for pattern in tech_patterns + soft_patterns:
        matches = re.findall(pattern, text_lower)
        found.extend(matches)
    # Extrair palavras com 4+ caracteres que parecem relevantes
    words = re.findall(r'\b[a-záàâãéêíóôõúç]{4,}\b', text_lower)
    found.extend(words[:50])  # Limitar para evitar ruído
    return list(set(found))


def calculate_match_score(profile_text: str, jd_text: str) -> dict:
    """Calcula o score de match entre perfil e job description."""
    profile_keywords = set(extract_keywords(profile_text))
    jd_keywords = set(extract_keywords(jd_text))

    if not jd_keywords:
        return {"score": 0, "matched": [], "missing": [], "percentage": 0}

    matched = profile_keywords.intersection(jd_keywords)
    missing = jd_keywords - profile_keywords
    percentage = (len(matched) / len(jd_keywords)) * 100

    return {
        "score": percentage,
        "matched": sorted(list(matched)),
        "missing": sorted(list(missing)),
        "percentage": round(percentage, 1),
        "total_jd_keywords": len(jd_keywords),
        "matched_count": len(matched),
    }


def classify_score(percentage: float) -> str:
    """Classifica o score de afinidade."""
    if percentage >= 70:
        return "ALTO (70%+) — Boa chance de avançar na triagem"
    elif percentage >= 40:
        return "MÉDIO (40–69%) — Atende requisitos mínimos, faltam diferenciais"
    else:
        return "BAIXO (<40%) — Gaps críticos, otimização necessária antes de candidatar"


def generate_report(profile_text: str, jd_text: str, candidate_name: Optional[str] = None) -> str:
    """Gera relatório completo de análise de match."""
    result = calculate_match_score(profile_text, jd_text)
    classification = classify_score(result["percentage"])

    report = []
    report.append("=" * 60)
    report.append("ANÁLISE DE MATCH — GUPY SPECIALIST")
    if candidate_name:
        report.append(f"Candidato: {candidate_name}")
    report.append("=" * 60)
    report.append("")
    report.append(f"📊 SCORE DE AFINIDADE ESTIMADO: {result['percentage']}%")
    report.append(f"   {classification}")
    report.append("")
    report.append(f"✅ PALAVRAS-CHAVE ENCONTRADAS ({result['matched_count']}/{result['total_jd_keywords']}):")
    if result["matched"]:
        for kw in result["matched"][:20]:
            report.append(f"   • {kw}")
    else:
        report.append("   Nenhuma palavra-chave da vaga encontrada no perfil.")
    report.append("")
    report.append(f"❌ PALAVRAS-CHAVE AUSENTES ({len(result['missing'])} termos):")
    if result["missing"]:
        for kw in list(result["missing"])[:20]:
            report.append(f"   • {kw}  ← Adicionar ao perfil se aplicável")
    else:
        report.append("   Excelente! Todas as palavras-chave estão presentes.")
    report.append("")
    report.append("💡 PRÓXIMAS AÇÕES RECOMENDADAS:")
    if result["percentage"] < 40:
        report.append("   1. Revisar completamente o perfil antes de candidatar")
        report.append("   2. Adicionar as palavras-chave ausentes nas seções Habilidades e Experiências")
        report.append("   3. Quantificar resultados nas experiências profissionais")
    elif result["percentage"] < 70:
        report.append("   1. Adicionar palavras-chave ausentes em Habilidades")
        report.append("   2. Revisar descrições de experiências para incluir termos da vaga")
        report.append("   3. Verificar critérios eliminatórios antes de candidatar")
    else:
        report.append("   1. Verificar critérios eliminatórios")
        report.append("   2. Candidatar-se nas primeiras 24–48h da publicação")
        report.append("   3. Preparar-se para os testes cognitivos e comportamentais")
    report.append("")
    report.append("=" * 60)
    return "\n".join(report)


def main():
    print("=== GUPY MATCH ANALYZER ===")
    print("Cole o texto do JOB DESCRIPTION (pressione Enter duas vezes para finalizar):")
    jd_lines = []
    while True:
        line = input()
        if line == "" and jd_lines and jd_lines[-1] == "":
            break
        jd_lines.append(line)
    jd_text = "\n".join(jd_lines)

    print("\nCole o texto do seu PERFIL/CURRÍCULO (pressione Enter duas vezes para finalizar):")
    profile_lines = []
    while True:
        line = input()
        if line == "" and profile_lines and profile_lines[-1] == "":
            break
        profile_lines.append(line)
    profile_text = "\n".join(profile_lines)

    if not jd_text.strip() or not profile_text.strip():
        print("Erro: É necessário fornecer tanto o job description quanto o perfil.")
        sys.exit(1)

    report = generate_report(profile_text, jd_text)
    print("\n" + report)


if __name__ == "__main__":
    main()
