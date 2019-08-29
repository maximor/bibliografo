%Archivo que se encargara de la generacion de libros, los hechos de los libros tendran:
% el nombre, autor,categoria o genero,precio, fecha comoun hecho
% publicacion o hace cuanto dias se publico y tambien cuanta estrellas
% tiene, estado del libro

%Hechos
%:-dynamic libro/8.
:-dynamic bibliografo/2.
%bibliografo(Nombre,Sueldo,Porcentaje,Ingreso)
:-dynamic fecha/3.
:-dynamic bibliografo/2.
:-dynamic bibliografoEx/2.
:-dynamic filtrodb/6.
:-dynamic ingresoExtra/3.
:-dynamic disponible/1.
:-dynamic resultado/1.
:-dynamic temporal/1.

%Libro(Titulo,Autor,Genero,Precio,Fecha,Raiting,Estado,ISBN)

libro('Lo que el viento se llevo','Carol Mitchel',['romantico','historico'],700,date(2019,08,15),4.5,nuevo,78965412365987415).
libro('Salvage y apasionado','Emili Sant',['romantico','sensual'],300,date(2007,06,3),4,nuevo,8748945412365987415).
libro('Amor Real','Roseluana',['romantico'],1000,date(2013,07,10),3,usado,7896557487948484498).
libro('Tengo miedo de la noche','Maximilian Torner',['real','misterio','Suspenso'],250,date(2015,03,15),4.7,nuevo,78549684894898499).
libro('Te mire y te ame','Karvin Santos',['romantico'],300,date(2015,06,20),4,usado,78965454684848968).

%Reglas
pertenece(X,[X|_]).
pertenece(X,[_|Cola]):-pertenece(X,Cola).

%Con esta regla se podra actualizar el sueldo del bibliografo
actualizarSueldo(X):-bibliografo(Y,_),Y=Q,retract(bibliografo(_,_)),assert(bibliografo(Q,X)),write('EL nuevo sueldo es'),tab(3),write(X).

actualizarDisponible(Disponible):-retractall(disponible(X)),assert(disponible(Disponible)).
% Con esta regla se van a sumar los ingresos extras todos los ingresos
% filtrados por el mes que le envie el usuario- Tratar de hacer que se
% filtre con la fecha tomando el mes basado en el dia de hoy

sumarIngreso(Mes,Total):-aggregate_all(sum(Ingreso),ingresoExtra(_,Ingreso,Mes),Total).

% Las preguntas de esta regla deberia estar en el programa de prolog y
% aqui llegar con la opcion de que desea usar elejida para solamente
% verificar la eleccion y hacer los calculos
disponiblecompra(Sueldo,Porcentaje,_,1):-Disponible is (Sueldo*(Porcentaje/100)),actualizarDisponible(Disponible),!.
disponiblecompra(_,_,IngresoExtra,2):-actualizarDisponible(IngresoExtra),!.
disponiblecompra(Sueldo,Porcentaje,IngresoExtra,3):-Disponible is (IngresoExtra + (Sueldo*(Porcentaje/100))),assert(disponible(Disponible)),!.


% Este mes me entraron adicionalmente a mi sueldo 5,500 pesos. �Qu�
% libros que han salido hace menos de 7 d�as puedo adquirir con eso? �
% Con los 3,500 que me entraron este mes, m�s el 10% de mi sueldo, �Qu�
% libros etiquetados como ciencia ficci�n o historia con 4 estrellas o
% m�s puedo adquirir? � Usa mis entradas adicionales para decirme que
% libros puedo comprarme que sean usados y que el 50% de ellos est�
% etiquetado en m�s de una categor�a. � �Qu� libros etiquetados como
% econom�a puedo comprarme con el 20% de mi sueldo, cuyo autor sea Edward
% Conard y que en el t�tulo no tengan la palabra crisis? � �Cu�ntos
% libros etiquetados como viaje han salido este mes que tengan una
% puntuaci�n de 5 estrellas, independientemente que sean nuevos o usados?


filtro(Titulo,Autor,Genero,Precio,Fecha,Raiting,Estado,ISBN):-retractall(resultado(X)),
     libro(Tit,Aut,Gen,Precio,Fecha,Rai,Estado,ISBN),
    ((not(Titulo=Tit)->sub_string(Tit,_,_,_,Titulo));Titulo=Tit),
    ((not(Autor=Aut)->sub_string(Aut,_,_,_,Autor));Autor=Aut),
    pertenece(Genero,Gen),
    ((not(Rai=Raiting)->Rai>=Raiting);Rai=Raiting),
    disponible(Dinero),
    Precio=<Dinero,
    Resultado=libro(Tit,Autor,Gen,Precio,Fecha,Rai,Estado,ISBN),
    write(Resultado),nl,assert(resultado(Resultado)),fail.

nofiltro(Titulo,_,_,_,_,_,_,_,1):-resultado(libro(Tit,Autor,Gen,Precio,Fecha,Raiting,Estado,ISBN)),retract(resultado(libro(Tit,Autor,Gen,Precio,Fecha,Raiting,Estado,ISBN))),
    not((sub_string(Tit,_,_,_,Titulo))),
    asserta(resultado(libro(Tit,Autor,Gen,Precio,Fecha,Raiting,Estado,ISBN))),write(libro(Tit,Autor,Gen,Precio,Fecha,Raiting,Estado,ISBN)),nl,fail,!.

nofiltro(_,Autor,_,_,_,_,_,_,2):-resultado(libro(Tit,Aut,Gen,Precio,Fecha,Raiting,Estado,ISBN)),retract(resultado(libro(Tit,Aut,Gen,Precio,Fecha,Raiting,Estado,ISBN))),
    not((sub_string(Aut,_,_,_,Autor))),
    asserta(resultado(libro(Tit,Aut,Gen,Precio,Fecha,Raiting,Estado,ISBN))),write(libro(Tit,Autor,Gen,Precio,Fecha,Raiting,Estado,ISBN)),nl,fail,!.

nofiltro(_,_,Genero,_,_,_,_,_,3):-resultado(libro(Tit,Aut,Gen,Precio,Fecha,Raiting,Estado,ISBN)),retract(resultado(libro(Tit,Aut,Gen,Precio,Fecha,Raiting,Estado,ISBN))),
    not(pertenece(Genero,Gen)),
    asserta(resultado(libro(Tit,Aut,Gen,Precio,Fecha,Raiting,Estado,ISBN))),write(libro(Tit,Aut,Gen,Precio,Fecha,Raiting,Estado,ISBN)),nl,fail,!.

nofiltro(_,_,_,_,_,_,Estado,_,4):-resultado(libro(Tit,Aut,Gen,Precio,Fecha,Raiting,Est,ISBN)),retract(resultado(libro(Tit,Aut,Gen,Precio,Fecha,Raiting,Est,ISBN))),
    not(Estado=Est),
    asserta(resultado(libro(Tit,Aut,Gen,Precio,Fecha,Raiting,Est,ISBN))),write(libro(Tit,Aut,Gen,Precio,Fecha,Raiting,Est,ISBN)),nl,fail,!.





% nofiltro(Titulo,Autor,Genero,Precio,Fecha,Raiting,Estado,ISBN,Resultado):-resultado(libro(Titulo,Autor,Genero,Precio,Fecha,Raiting,Estado,ISBN)),
%
    %(not(((Titulo=Tit)->sub_string(Tit,_,_,_,Titulo)))),
    %not(pertenece(Genero,Gen)),
    %(not((((Autor=Aut)->sub_string(Aut,_,_,_,Autor))))),
    %disponible(Dinero),Precio=<Dinero,Resultado=libro(Tit,Autor,Gen,Precio,Fecha,Raiting,Estado,ISBN),
    %write(Resultado),nl,fail.


