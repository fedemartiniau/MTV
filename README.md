## MTV
MultyToolViewer
Version 0.0.1

# Instalacion
1.- Instalar con configuracion por defecto Anaconda (tei-console\tools\Anaconda3-5.3.1-Windows-x86_64.exe)
2.- Desde el menu de inicio de windows abrir la consola de Anaconda Prompt
3.- Instalar pika (pip install pika)
3.- Instalar protobuf (pip install protobuf)


# Ejecutar
1.- Desde el menu de inicio de windows abrir la consola de Anaconda Prompt
2.- Posicionarse dentro de la carpeta en la que se encuentra el archivo "teiviewer.py" (\tei-console\tei-console)


# Informacion para el uso
Está es una maqueta de la propuesta de visualizador de telemetría usando python y pyqt.
La propuesta es proporcionar una ventana “padre” cuyo contenido se arma según necesidad a partir de un archivo XML. El contenido de la página será a partir de widgets. Estos widgets estarán contenidos dentro de tabs de la ventana “padre”.
En estos momentos solo hay tres widgets “MultiPlot”, "Grid" y "Label"
* MultiPlot: Es un gráfico que puede representar una o varias variables
* Grid: Es una tabla tipo planilla de Excel donde se puede asociar las variables a una celda específica. 
* Label: Solo mostrará la variable y el valor.

## Estructura de XML
		<view>
			<tab name="NombreTab1">
				<recuadro gillaX="1" gillaY="1" filas="1" columnas="1">	
					<widget type="TipoWidget" title="">
						<tmyvar name="VARIABLE" compare="False" max="500" min="0" color-nominal="#c5c9c7" color-error="#c5c9c7" sombra="False" color-sombra="#54bad0"/>
					</widget>
				</recuadro>
			</tab>
		</view>

Todo el contenido del XML debe estar dentro de la etiqueta “view”, luego en ella deben estar listados los tabs:

		<view>
			<tab name="NombreTab1">	</tab>
			<tab name="NombreTab2">	</tab>
			<tab name="NombreTab3">	</tab>
						…..
			<tab name="NombreTabN">	</tab>
		</view> 

En la ventana cada tab está dividido en una grilla de 6 columnas por 4 filas, por lo que cada widget deberá estar definido dentro de está grilla y por lo que necesita la etiqueta recuadro para indicar que hay dentro de él.
		<tab name="NombreTab1">
			<recuadro gillaX="1" gillaY="1" filas="1" columnas="1">	</recuadro>
			<recuadro gillaX="1" gillaY="2" filas="1" columnas="1">	</recuadro>
			<recuadro gillaX="1" gillaY="3" filas="1" columnas="1">	</recuadro>
							…..
			<recuadro gillaX="4" gillaY="6" filas="1" columnas="1">	</recuadro>
		</tab> 

Con los parametros del tag definimos en que recuadro se ubicará y en cuantas filas y columnas usara. 
Recuadro 
	gillaX="1"  posicion en x
	gillaY="2" posicion en y
	filas="1" canidad de filas que ocupa
	columnas="1" cantidad de columnas que ocupa

**Nota: Los recuadros solo ocupan lugar si tienen contenido. 

Dentro de cada recuadro pondremos el widget 

		<recuadro gillaX="1" gillaY="1" filas="1" columnas="1">
			<widget type="MultiPlot" title="Grafico Inferior">
				<tmyvar name="VARIABLE_DUMMY_6" compare="False" max="20000" min="0" color-nominal="#c5c9c7" color-error="#c5c9c7" sombra="False" color-sombra="#54bad0" />
			</widget>
		</recuadro>

Cada widget tiene configuración propia:


* Label:
		<widget type="Label">
			<tmyvar name="VARIABLE_DUMMY_8"  />
		</widget>
Definimos el nombre de la variable

* MultiPlot: 
		<widget type="MultiPlot" title="Grafico 4">
			<tmyvar name="Cotroller_Status_04" compare="True" max="45" min="-45" color-nominal="#71aa34" color-error="#fe2c54"   sombra="False" color-sombra="#54bad0"/>
		</widget>

		
	name="Cotroller_Status_04" 
		Nombre de la variable a buscar
	compare="True"
		Si vamos a comparar el valor de la variable con el máximo y el mínimo
	max="45" min="-45"
		Valores entre los que se considera que la variable estará nominal, fuera de esos límites se pone como error. 
	color-nominal="#71aa34"
	color-error="#fe2c54"
		se definen los colores según el estado de la variable
	sombra="False"
	color-sombra="#54bad0"
		Se define si en el gráfico se rellena el área debajo de la curva.



* Grid:
		<widget type="Grid" columns="4" rows="5">
			<tmyvar name="Status_1" column="1" row="1" compare="False" type="title" color-text="#87ae73" color-background="#87ae73"  />
			<tmyvar name="Cotroller_Status_01" column="1" row="2" compare="False" type="nuber" max="45" min="-45" color-nominal="#87ae73" color-error="#fe2c54"  unidad=""/>		<tmyvar name="var_1" column="2" row="4" compare="False" type="nuber"  value="ERROR"  color-nominal="#87ae73" color-error="#fe2c54"  unidad="cm"/>		
			<tmyvar name="Status_1" column="2" row="1" compare="True" type="text"  value="ERROR"  color-nominal="#87ae73" color-error="#fe2c54"  unidad=""/>
		</widget>

	Dentro de la definición del widget:
	columns="4" 
	rows="5"
		Define cuanuantas columnas y cuantas filas tiene la tabla

	Para las variables están los siguientes parámetros:
	name="Status_1" nombre de la variable 
	column="1"
	row="1"
		Posición en la tabla  

	compare="False" 
		Si se va verificar el valor de la variable
	type="" 
		Para las variables se pueden definir 3 tipos de datos:
	type="title"
		Title es un campo que solo se usa para mostrar un texto en la celda especificada

	type="nuber"
		Se usa para indicar que la variable es del tipo numérico
	max="45" 
	min="-45" 
		Valores extremos que definen el periodo nominal o de error
	color-nominal="#87ae73" color-error="#fe2c54"  
		Colores que toma la celda de la variable 
	unidad="cm"
		Le agrega el símbolo de la unidad al valor de la variable

	type="text" 
		Se usa para indicar que la variable es de tipo texto y se trate de esta manera
	value="ERROR"  
		Valor que busca para definir estado nominal o de error
	color-nominal="#87ae73" 
	color-error="#fe2c54"  
	unidad=""








