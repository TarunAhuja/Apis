# -*- coding: cp1252 -*-
import nltk
import re
sentence="""Una de las clases que m�s adeptos tiene en los gimnasios suele ser la de stretching o estiramientos, y es que estirar nuestros m�sculos es importante y beneficioso despu�s de realizar cualquier actividad f�sicaLas sesiones espec�ficas de stretching suelen durar entre 20 y 30 minutos, tiempo suficiente para estirar los m�sculos implicados en el deporte que acabamos de practicar. �Cu�les son las tres reglas de oro de los estiramientos? La primera regla, y posiblemente la m�s importante, es que durante nuestros estiramientos no debemos sentir dolor: solamente debemos notar resistencia. El dolor es un mecanismo de aviso de nuestro sistema nervioso para comunicarnos que se puede producir una lesi�n, y esto es precisamente lo que estamos tratando de evitar a trav�s de los estiramientos.Bien es cierto que hay personas que escud�ndose en la idea de no sentir dolor no realizan los ejercicios de estiramiento correctamente: debemos sentir una tensi�n moderada en el m�sculo que estamos estirando para que los estiramientos sean efectivos.La segunda regla del stretching es que los estiramientos deben ser mantenidos en el tiempo durante aproximadamente 20 o 30 segundos. Debemos estirar el m�sculo concreto y mantener esa tensi�n moderada durante un per�odo corto de tiempo para despu�s volver a relajarlo.Es importante que no realicemos movimientos bal�sticos (tirones r�pidos para llegar a la m�xima elongaci�n del m�sculo), ya que pueden provocar dolor o lesiones en el m�sculo. Los estiramientos bal�sticos son uno de los m�todo utilizados para trabajar la flexibilidad, aunque se les achaca que debido al tiempo reducido de estiramiento no existe una adaptaci�n neuromuscular.Personalmente, en las sesiones colectivas de stretching prefiero trabajar con movimientos controlados y mantenidos en el tiempo, que son m�s seguros y, a mi parecer, m�s efectivos para la poblaci�n media de los gimnasios.No podemos olvidar la correcta alineaci�n corporal y correcci�n postural durante los estiramientos. Mantener una postura correcta, por ejemplo, durante un ejercicio de articulaci�n de la columna, es vital para prevenir lesiones y sacar el m�ximo partido a nuestras sesiones de estiramientos.Las pautas suelen ser similares en todos los ejercicios: hombros atr�s y abajo, cintura escapular alineada, mirada al frente, pecho arriba, pelvis neutra� Son datos que debemos conocer y que el instructor debe transmitir a sus alumnos para llevar a cabo estiramientos seguros y efectivos.Y vosotros, �estir�is siempre al acabar vuestro entrenamiento?"""
text = nltk.word_tokenize(sentence)
tagged=nltk.pos_tag(text)
namedentities = nltk.chunk.ne_chunk(tagged,binary=True)
entities=re.findall(r'NE\s(.*?)/',str(namedentities))
print(entities)
