import pandas as pd

df = pd.read_csv("electronics_store_sales.csv")

df["product"] = df["product"].fillna("Unknown")

df['price'] = df.groupby('product')['price'].transform(lambda series: series.fillna(series.median()))

'''
1. count:
   - Jest to liczba niepustych (nie-null) wartości w każdej kolumnie.
   - Pomaga zrozumieć, ile ważnych punktów danych masz dla każdej cechy.

2. mean (średnia):
   - Jest to średnia arytmetyczna wszystkich wartości w kolumnie.
   - Daje pojęcie o centralnej tendencji danych.

3. std (odchylenie standardowe):
   - Mierzy stopień rozproszenia wartości.
   - Niskie odchylenie standardowe oznacza, że punkty danych zwykle są blisko średniej, podczas gdy wysokie odchylenie standardowe wskazuje, że są rozrzucone w szerszym zakresie.

4. min (minimum):
   - Najmniejsza wartość w kolumnie.
   - Przydatne do zrozumienia zakresu danych i identyfikacji potencjalnych wartości odstających.

5. 25% (pierwszy kwartyl):
   - 25% wartości jest poniżej tej liczby.
   - Pomaga zrozumieć rozkład niższych wartości w danych.

6. 50% (mediana):
   - Środkowa wartość, gdy dane są uporządkowane od najniższej do najwyższej.
   - W przeciwieństwie do średniej, nie jest podatna na skrajne wartości odstające, więc może być bardziej solidną miarą centralnej tendencji.

7. 75% (trzeci kwartyl):
   - 75% wartości jest poniżej tej liczby.
   - Pomaga zrozumieć rozkład wyższych wartości w danych.

8. max (maksimum):
   - Największa wartość w kolumnie.
   - Podobnie jak minimum, jest przydatne do zrozumienia zakresu i identyfikacji potencjalnych wartości odstających.

Te statystyki są szczególnie użyteczne do:

- Szybkiego przeglądu rozkładu danych.
- Identyfikacji potencjalnych wartości odstających (szukaj bardzo wysokich wartości max lub bardzo niskich min).
- Zrozumienia rozpiętości danych (używając odchylenia standardowego i kwartyli).
- Sprawdzania problemów z jakością danych (np. jeśli min i max wydają się nierozsądne dla tego, co reprezentuje kolumna).
'''

print(df.describe())