# Teoremas da Bissetriz Interna e Externa

## Parte A – Bissetriz Interna

### Hipótese do Teorema da Bissetriz Interna
**Hipótese:** Em um triângulo, a bissetriz de um ângulo divide o lado oposto em segmentos que são proporcionais aos lados adjacentes.

### Tese do Teorema da Bissetriz Interna
**Tese:** Se \( D \) é um ponto no lado \( BC \) de um triângulo \( ABC \), tal que a bissetriz do ângulo \( A \) intercepta \( BC \) em \( D \), então:
\[
\frac{BD}{DC} = \frac{AB}{AC}
\]

### Demonstração do Teorema da Bissetriz Interna
1. Considere o triângulo \( ABC \) com a bissetriz \( AD \) dividindo o lado \( BC \) em \( BD \) e \( DC \).
2. Forme os triângulos \( ABD \) e \( ACD \).
3. Os ângulos \( \angle ADB \) e \( \angle ADC \) são iguais, pois \( AD \) é a bissetriz.
4. Aplicando a semelhança de triângulos (critério AA), temos:
   \[
   \frac{AB}{AC} = \frac{BD}{DC}
   \]

### Sugestão de Implementação em Python para Bissetriz Interna
O código já foi implementado na versão anterior e calcula a razão das partes formadas pela bissetriz interna no lado oposto.

---

## Parte B – Bissetriz Externa

### Hipótese do Teorema da Bissetriz Externa
**Hipótese:** Em um triângulo, a bissetriz externa de um ângulo divide o lado oposto em segmentos que são proporcionais aos lados adjacentes.

### Tese do Teorema da Bissetriz Externa
**Tese:** Se \( D \) é um ponto fora do triângulo \( ABC \) tal que a bissetriz do ângulo \( A \) intercepta a extensão do lado \( BC \) em \( D \), então:
\[
\frac{BD}{DC} = \frac{AB}{AC}
\]

### Demonstração do Teorema da Bissetriz Externa
1. Considere o triângulo \( ABC \) e a bissetriz externa \( AD \).
2. Os triângulos \( ABD \) e \( ACD \) são formados, onde \( D \) está fora do triângulo.
3. Os ângulos \( \angle ADB \) e \( \angle ADC \) são iguais.
4. Aplicando a semelhança de triângulos, temos:
   \[
   \frac{AB}{AC} = \frac{BD}{-DC}
   \]

### Sugestão de Implementação em Python para Bissetriz Externa
A mesma lógica do código anterior se aplica aqui, calculando a divisão do lado oposto pela bissetriz externa.

---

## Parte C – Condições para Intersecção da Bissetriz Externa

### Condições de Intersecção
A bissetriz externa intercepta o lado oposto quando o lado oposto é prolongado. A condição para que a bissetriz externa realmente atinja o lado oposto é que o lado do triângulo deve ser maior que a diferença dos outros dois lados. Matematicamente, se \( a \) e \( b \) são os lados adjacentes ao ângulo e \( c \) é o lado oposto:
\[
c > |a - b|
\]

### Justificação
Se a condição acima for verdadeira, a bissetriz externa encontrará o lado oposto em um ponto \( D \) que divide o lado \( BC \) em segmentos que são proporcionais aos lados adjacentes.