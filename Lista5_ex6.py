def converterTempo(segundos):
    horas = segundos // 3600
    resto = segundos % 3600
    minutos = resto // 60
    segundos = resto % 60
    
    print(f"Tempo de duração: {horas}h {minutos}m {segundos}s")
teste = converterTempo(36472)