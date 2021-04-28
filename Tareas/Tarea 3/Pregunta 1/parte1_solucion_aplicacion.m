function parte1_solucion_aplicacion()
  
  %Esta función se encarga de insertar los datos del problema para ingeniería elegido en los métodos del paquete NumInt
  %
  %Sintaxis: parte1_solucion_aplicacion()
  
  pkg load numint
  output_precision(15)
  warning("off","all")

  f = "1/(9.8-0.3226*x)";
  a = 0; %Limite inferior de la integral
  b = 10; %Limite supeior de la integral
  n = 5; %Numero de subintervalos para 'trapecio_compuesto' y 'simpson_compuesto'
  m = 3; %Grado del polinomio de Legendre 'gaussiana' y 'gaussiana_compuesta'
  n_romberg = 5; %Cantidad de filas de la tabla de Romberg a realizar

  I_exacta = 1.237631464459078;

  display("trapecio")
  t = now();
  I = trapecio(f, a, b)
  ExecTime = now()-t
  Error = abs(I-I_exacta)


  display("simpson")
  t = now();
  I = simpson(f, a, b)
  ExecTime = now()-t
  Error = abs(I-I_exacta)

  display("trapecio_compuesto")
  t = now();
  I = trapecio_compuesto(f, a, b, n)
  ExecTime = now()-t
  Error = abs(I-I_exacta)

  display("simpson_compuesto")
  t = now();
  I = simpson_compuesto(f, a, b, n)
  ExecTime = now()-t
  Error = abs(I-I_exacta)

  display("gaussiana")
  t = now();
  I = gaussiana(f, a, b, m)
  ExecTime = now()-t
  Error = abs(I-I_exacta)

  display("gaussiana_compuesta")
  t = now();
  I = gaussiana_compuesta(f, a, b, m, m)
  ExecTime = now()-t
  Error = abs(I-I_exacta)

  display("romberg")
  t = now();
  I = romberg(f, a, b, n_romberg)
  ExecTime = now()-t
  Error = abs(I-I_exacta)
  
end