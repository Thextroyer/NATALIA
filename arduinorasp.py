

#variable para almacenar el mensaje
#le asignamos un valor introducido por el usuario
print "Introduce un caracter ('s' para salir): "
entrada = raw_input()

while entrada != 's': #introduciendo 's' salimos del bucle

   ser.write(entrada) #envia la entrada por serial
   print "He enviado: ", entrada
   print "Introduce un caracter ('s' para salir): "

   entrada = raw_input() #introduce otro caracter por teclado


#CÓDIGO ARDUINO
   #define LED 13
   int mssg = 0; //variable para guardar el mensaje

   void setup()
   {
      pinMode(LED, OUTPUT); //establecemos 13 como salida
      Serial.begin(9600); //iniciando Serial
   }

   void loop()
   {
      if (Serial.available() > 0)
      {
         mssg = Serial.read(); //leemos el serial

         if(mssg == 'e')
         {
            digitalWrite(13, HIGH); //si entra una 'e' encendemos
         }
         else if(mssg == 'a')
         {
            digitalWrite(13, LOW); //si entra una 'a' apagamos
         }
      }
   }


Encontrando puerto serial donde se encuentra el arduino
Para encontrar dónde está ubicado tu arduino, puedes hacer un primer chequeo. En este caso verificar que hay algún puerto serial disponible teniendo una ruta patrón tipo /dev/ttyUSB o /dev/ttyAMC. Esto lo puedes hacer desde consola con el comando ls.


ls /dev/ttyUSB*
ls /dev/ttyACM*
1
2
ls /dev/ttyUSB*
ls /dev/ttyACM*
Luego para hacer una última verificación puedes utilizar el comando:

Shell

dmesg | tail -3
1
dmesg | tail -3
