# Trabajo práctico agentes racionales
## Ejercicio C
#### Pruebas agente simple

Cantidad de cuadros recorridos:

| Entornos/cuadros | 2x2  | 4x4 | 8x8 | 16x16 | 32x32 | 64x64 | 128x128 |
|--------|--------|--------|--------|--------|--------|--------|--------|
|0.1     |1 de 1|0 de 2|0 de 6|18 de 26|77 de 102|95 de 410|80 de 1638|
|0.2     |1 de 1|3 de 3|9 de 13|16 de 51|145 de 205|183 de 819|174 de 3277|
|0.4     |2 de 2|1 de 6|9 de 26|52 de 102|142 de 410|198 de 1638|314 de 6554|
|0.8     |3 de 3|8 de 13|9 de 51|37 de 205|371 de 819|549 de 3277|542 de 13107|

Porcentaje de cuadros recorrido:

| Entornos/cuadros | 2x2  | 4x4 | 8x8 | 16x16 | 32x32 | 64x64 | 128x128 |
|--------|--------|--------|--------|--------|--------|--------|--------|
|0.1     |100%    |0%     |0%      |69.23%  |75.49%  |23.17%  |4.88%   |
|0.2     |100%	  |33%    |69.23%  |31.37%  |70.73%  |22.34%  |5.31%   |
|0.4     |100%    |16.67% |34.62%  |50.98%  |34.63%  |12.09%  |4.79%   |
|0.8     |100%    |61.54% |17.62%  |18.05%  |45.3%   |16.75%  |4.14%   |
## Ejercicio D
#### Pruebas agente random
Cantidad de cuadros recorridos:

| Entornos/cuadros | 2x2  | 4x4 | 8x8 | 16x16 | 32x32 | 64x64 | 128x128 |
|--------|--------|--------|--------|--------|--------|--------|--------|
|0.1     |1 de 1|2 de 2|6 de 6|17 de 26|27 de 102|37 de 410|31 de 1638|
|0.2     |1 de 1|3 de 3|13 de 13|43 de 51|41 de 205|48 de 819|42 de 3277|
|0.4     |2 de 2|5 de 6|18 de 26|53 de 102|93 de 410|79 de 1638|81 de 6554|
|0.8     |3 de 3|10 de 13|33 de 51|77 de 205|185 de 819|137 de 3277|153 de 13107|

Porcentaje de cuadros recorrido:

| Entornos/cuadros | 2x2  | 4x4 | 8x8 | 16x16 | 32x32 | 64x64 | 128x128 |
|--------|--------|--------|--------|--------|--------|--------|--------|
|0.1     |100%    |100%    |100%    |65.38%  |26.47%  |9.02%   |1.89%   |
|0.2     |100%	  |100%    |100%    |84.31%  |20%     |5.49%   |1.28%   |
|0.4     |100%    |83.33%  |69.23%  |51.96%  |22.68%  |4.82%   |1.24%   |
|0.8     |100%    |76.92%  |64.71%  |37.56%  |22.59%  |4.18%   |1.17%   |

## Ejercicio E
#### 2.9)
**a)** No es posible ya que el agente es incapaz de encontrar el camino con menos pasos posibles.

**b)** En caso de un agente con estados si sería racional ya que el agente sabe por cuales cuadros ha pasado, evitando repetirlos en el proceso.

**c)** Suponiendo que la información sólo da la cantidad de cuadros sucios (o limpios), el agente simple seguiría sin ser racional ya que no es capaz de saber por cuales pasó y por cuales no, repitiendo movimientos en el proceso.
Por otro lado, con esa información es posible hacer un algoritmo más eficiente ya que, por ejemplo, es posible hacer que pare cuando limpie todas. En definitiva seguirá siendo racional.

#### 2.10)

**a)** No, ya que lo único que el algoritmo va a poder hacer es moverse sin un sentido en especial.

**b)** Puede ya que tiene mas posibilidades de moverse hacia cuadros sucios que el reflexivo normal. El reflexivo normal probablemente se quedaría chocando contra una pared, mientras que el aleatorio puede escapar de ese loop infinito.

**c)** Mientras más grande sea el mapa, peor se comportará el aleatorio, ya que perderá ciclos de vida intentando limpiar o quedandose quieto.

**d)** Puede ya que es capaz de guardar información sobre el mundo y evitar tomar las mismas desciciones una y otra vez.
