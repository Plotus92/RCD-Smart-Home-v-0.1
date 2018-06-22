# RCD-Smart-Home-v-0.1
Project Python arduino by Julius Quast and Jonas Zoellner

The Doxygen file of the arduino part is in the wifi_setup folder.
I cloned the .ino file into a .c file, because doxygen didn't work with otherwise.

The Doxygen file of Python are in Doxygen Python Files.rar

User Guide :

Step 1 : Verbinden sie den Aufbau mit einer Stromquelle (Powerbank,Batterie,Latop,etc). Der Laser wird unabhängig angeschlossen und auf den Fotowiderstand gerichtet.

Step 2 : Starten sie das Python Programm (Server + Application 2.0) und warten sie, bis der Server onlinen ist. Im Command Fenster sollte stehen Suche clients  Your IP : 3030

Step 3 : Drücken sie den Button im Arduino Versuchsaufbau. Nun sollte in ihrerm Python Command Fenster stehen, dass sich ein Client verbunden hat.

Step 4 : Wenn nun die Lichtschranke unterbrochen wird, sendet der Arduino eine Variable an den Python Server und dieser reagiert entsprechend darauf und sendet an den Arduino zurück. Dieser führt dann etwas aus. In userem Falle wird ein Licht an oder aus gemacht.

Anmerkung : Man kann natürlich statt eines Lichtes auch andere Verwendungszwecke ausführen lassen. Wir wollten mit dem Licht Anwedungsbeispiel nur die Funktion demonstrieren.
