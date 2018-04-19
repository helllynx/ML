# Cijfer Handschrift Herkenning

In dit document beschrijf ik de werking van dit project wat geschreven cijfers herkent en aangeeft welk
number het beste overeenkomt met de input.

Het project maakt gebruik van Tenserflow om te trainen, hierbij worden datasets van 'MNIST_data' gebruikt
en 'Tensorflow_in_ROS', een project op Github (https://github.com/shunchan0677/Tensorflow_in_ROS) voor
het raden van nummers aan de hand van een camera op het ROS platform.

## Trainen

Standaard wordt het project geleverd met een al uitgevoerde training. Het is dus in principe niet nodig
om zelf het netwerk nog te trainen. Dit netwerk heeft een accuraatheid van 99.2%. Mocht je het wel zelf
willen trainen dan kan dit. Er is een Python-programma 'train.py' welke je hierbij helpt. Deze gebruikt 
de data van 'MNIST_data' en traint op basis hiervan het programma. Ook is het mogelijk een eigen set
van afbeeldingen aan te leveren.

Bij het trainen worden de resultaten opgeslagen in een model, dit model kan je dus overnemen uit de 
repository of zelf opbouwen. In beide gevallen krijg je een bestand. Dit bestand kan weer ingevoerd worden
in de applicatie voor het testen.

## Aanpassingen

De reden dat ik voor deze applicatie heb gekozen is omdat het relatief simpel is met een praktisch 
voorbeeld van de toepassing. Echter hoef ik niet direct gebruik te maken van het ROS platform (kan wel
handig zijn mocht je dit willen gebruiken in combinatie met het Robotica project van Technische Informatica).

Om te zorgen dat de applicatie draait zonder ROS is het nodig een aantal aanpassingen te doen aan het programma. Zorg 
er in ieder geval voor dat je alle bestanden hebt gedownload van de GIT repository. Het trainen via 'train.py' vereist
geen aanpassingen, dit staat al los van het ROS-platform. Wel is het nodig 'tensorflow_in_ros_mnist.py' aan te passen.

1. Begin met het verwijderen van de dependenties bovenaan:

<pre>
<b>import rospy</b>
<b>from sensor_msgs.msg import Image</b>
<b>from std_msgs.msg import Int16</b>
<b>from cv_bridge import CvBridge</b>
import cv2
import numpy as np
import tensorflow as tf
</pre>

(Verwijder de dikgedrukte libraries)

2. Dan is er een klasse 'class RosTensorFlow()', hierin moeten ook een aantal wijzigingen worden gedaan:

Verwijder de regel <pre>self._cv_bridge = CvBridge()</pre>, welke nodig is voor ROS om de afbeeldingen te 
verwerken met openCV.

Dan kunnen de volgende regels ook weg, welke te maken hebben met data verwerking op ROS:
<pre>
self._sub = rospy.Subscriber('image', Image, self.callback, queue_size=1)
self._pub = rospy.Publisher('result', Int16, queue_size=1)
</pre>

En dan nog laatste restanten die ook wegkunnen:

<pre>
self._pub.publish(answer)

...

def main(self):
    rospy.spin()
    
...

rospy.init_node('rostensorflow')
</pre>

3. Dan passen we de applicatie wat aan, want de situatie die we willen is dat we een afbeelding in een functie 
kunnen stoppen en dat we daar dan uit krijgen welk getal in die afbeelding staat.

Eerst veranderen we de naam van de klasse 'RosTensorFlow()' naar 'handwritingDetection()'. Dan moet je het volgende 
opzoeken:

<pre>
tensor = RosTensorFlow()
tensor.main()
</pre> 

En dat veranderen we dan in:

<pre>
detector = handwritingDetection()
print(detector.detect('cijfer.png'))
print(detector.detect('cijfer2.png'))
</pre> 

Dan hoeven we alleen nog de herkennings-functie aan te passen.

4. Om de 'detect'-functie te schrijven gebruiken we grotendeels de code van <pre>def callback(self, image_msg):</pre>.
Deze 'callback'-functie gaan we hernoemen naar 'detect', en het tweede argument hernoemen we van 'image_msg' naar 
'imgLocation'. Het gaat er dus dan als volgt uitzien: <pre>def detect(self, imgLocation):</pre>.

Dan gaan we de afbeelding inladen, daarvoor kunnen een aantal regels weg:

<pre>
cv_image = self._cv_bridge.imgmsg_to_cv2(image_msg, "bgr8")
cv_image_gray = cv2.cvtColor(cv_image, cv2.COLOR_RGB2GRAY)
</pre>

en laden we op onze eigen manier een afbeelding in:

<pre>
cv_image = cv2.imread(imgLocation, 0)
</pre>

(plaats deze dus op de plek van de vorige twee.)

Dan hoeven we alleen nog alle verwijzingen naar 'cv_image_gray' te veranderen in 'cv_image'.

5. Om nu te testen hebben we al wat code neergezet, namelijk het volgende:

<pre>
print(detector.detect('cijfer.png'))
print(detector.detect('cijfer2.png'))
</pre>

Hierin verwijs je dan naar een afbeelding (in dit geval cijfer.png en cijfer2.png, welke gewoon png's zijn van 300 bij 
300 pixels met een enkel getekend getal erin) en deze functie geeft dan het waargenomen getal terug.




Dit is praktisch voorbeeld van wat mogelijk is met Tensorflow. De volledige sourcecode van hoe dit werkt is opgenomen 
in de repository maar kan wat moeilijk te begrijpen zijn. Wel is het een van de 'makkelijkste' voorbeelden omdat je
duidelijk kan zien wat er gebeurt.