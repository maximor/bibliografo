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
libro('The Fellowship of the Ring' ,'J.R.R. Tolkien',['fantasia','epica','viaje'],500,date(2019,8,21),4.35,nuevo,0618346252).
libro('The Two Towers' ,'J.R.R. Tolkien',['fantasia','epica','viaje'],550,date(2019,8,21),4.44,nuevo,0618346260).
libro('The Return of the King' ,'J.R.R. Tolkien',['fantasia','epica','viaje'],550,date(2019,8,20),4.52,nuevo,0345339738).
libro('Silmarilion' ,'J.R.R. Tolkien',['fantasia','epica'],500,(2019,8,24),3.91,nuevo,0345339738).

libro('Harry Potter and the Sorcerers Stone' ,'J.K. Rowling',['fantasia','epica'],575,date(2019,8,11),4.47,nuevo,0439554934).
libro('Harry Potter and the Chamber of Secrets' ,'J.K. Rowling',['fantasia','epica'],525,date(2019,8,12),4.41,nuevo,0439064864).
libro('Harry Potter and the Prisoner of Azkaban' ,'J.K. Rowling',['fantasia','epica'],640,date(2019,8,11),4.56,nuevo,0439655484).
libro('Harry Potter and the Goblet of Fire' ,'J.K. Rowling',['fantasia','epica'],700,date(2019,8,16),4.55,nuevo,043965587).
libro('Harry Potter and the Order of the Phoenix' ,'J.K. Rowling',['fantasia','epica'],610,date(2019,8,19),4.49,nuevo,0439358078).
libro('Harry Potter and the Half-Blood Prince'  ,'J.K. Rowling',['fantasia','epica'],675,date(2019,8,19),4.56,nuevo,0439785960).
libro('Harry Potter and the Deathly Hallows' ,'J.K. Rowling',['fantasia','epica'],750,date(2019,8,22),4.62,nuevo,0545010225).
libro('Harry Potter and the Cursed Child: Parts One and Two' ,'J.K. Rowling',['fantasia','epica'],710,date(2019,8,29),3.66,nuevo,0751565350).

libro('The Lion, the Witch and the Wardrobe','C.S. Lewis',['fantasia','epica','viaje'],525,date(2019,8,29),4.21,nuevo,457415777).
libro('Prince Caspian' ,'C.S. Lewis',['fantasia','epica','viaje'],565,date(2019,8,19),3.97,nuevo,000720230).
libro('The Voyage of the Dawn Treader','C.S. Lewis',['fantasia','epica','viaje'],570,date(2019,8,09),4.09,nuevo,006112527).
libro('The Silver Chair' ,'C.S. Lewis',['fantasia','epica','viaje'],525,date(2019,8,09),3.96,nuevo,457445277).
libro('The Horse and His Boy','C.S. Lewis',['fantasia','epica','viaje'],550,date(2019,8,17),3.91,nuevo,0439861365).
libro('The Magicians Nephew','C.S. Lewis',['fantasia','epica','viaje'],560,date(2019,8,18),4.03,nuevo,0060764902).
libro('The Last Battle','C.S. Lewis',['fantasia','epica','viaje'],575,date(2019,8,29),4.03,nuevo,0007202326).

libro('The Hunger Games','Suzanne Collins',['ciencia','ficcion'],630,date(2019,8,07),4.33,usado,0439023483).
libro('Catching Fire','Suzanne Collins',['ciencia','ficcion'],630,date(2019,8,09),4.29,usado,0439023491).
libro('Mockingjay','Suzanne Collins',['ciencia','ficcion'],675,date(2019,8,04),4.03,usado,0439023513).

libro('Divergent' ,'Veronica Roth',['ciencia','ficcion'],620,date(2019,8,19),4.21,usado,0062024035).
libro('Insurgent' ,'Veronica Roth',['ciencia','ficcion'],650,date(2019,8,29),4.05,usado,0007442912).
libro('Allegiant' ,'Veronica Roth',['ciencia','ficcion'],570,date(2019,8,09),3.63,usado,0007524277).

libro('A Game of Thrones' ,'George R.R. Martin',['fantasia','epica'],700,date(2019,8,27),4.45,usado,0553588486).
libro('A Clash of Kings'  ,'George R.R. Martin',['fantasia','epica'],710,date(2019,8,28),4.41,usado,0553381695).
libro('A Feast for Crows' ,'George R.R. Martin',['fantasia','epica'],680,date(2019,8,29),4.13,usado,0553588486).
libro('A Dance with Dragons' ,'George R.R. Martin',['fantasia','epica'],650,date(2019,8,05),4.32,usado,055358845676).
libro('The Winds of Winter' ,'George R.R. Martin',['fantasia','epica'],650,date(2019,8,06),4.41,usado,0002247410).

libro('The Upside of Inequality: How Good Intentions Undermine the Middle Class' ,'Edward Conard',['economia'],650,date(2019,8,16),3.28,nuevo,1595231234).
libro('Unintended Consequences: Why Everything You ve Been Told About the Economy Is Wrong ' ,'Edward Conard',['economia'],650,date(2019,8,18),3.39,nuevo,1591845505).

libro('They Called Us Enemy ' ,' George Takei',['historia'],650,date(2019,8,20),4.46,nuevo,1603094504).
libro('George Marshall: Defender of the Republic ' ,' David L. Roll',['historia'],725,date(2019,8,10),4.54,nuevo,110199097).
libro('Shanghai Dream' ,'  Philippe Thirault',['historia'],745,date(2019,8,06),4.50,usado,9781643378510).
libro('Bodies in Blue: Disability in the Civil War North' ,'Sarah Handley-Cousins',['historia'],715,date(2019,8,06),4.50,usado,0820355194).
libro('Socialism Sucks: Two Economists Drink Their Way Through the Unfree World ' ,' Robert A. Lawson',['historia'],745,date(2019,8,16),4.14,usado,162157945).


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


% Este mes me entraron adicionalmente a mi sueldo 5,500 pesos. ¿Qué
% libros que han salido hace menos de 7 días puedo adquirir con eso? •
% Con los 3,500 que me entraron este mes, más el 10% de mi sueldo, ¿Qué
% libros etiquetados como ciencia ficción o historia con 4 estrellas o
% más puedo adquirir? • Usa mis entradas adicionales para decirme que
% libros puedo comprarme que sean usados y que el 50% de ellos esté
% etiquetado en más de una categoría. • ¿Qué libros etiquetados como
% economía puedo comprarme con el 20% de mi sueldo, cuyo autor sea Edward
% Conard y que en el título no tengan la palabra crisis? • ¿Cuántos
% libros etiquetados como viaje han salido este mes que tengan una
% puntuación de 5 estrellas, independientemente que sean nuevos o usados?


% Filtro general, es un filtro que soporta varios parametros y por de
% facto restringe el precio a que se ajuste al ingreso extra.
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


%Filtro para Restringir el Titulo
nofiltro(Titulo,_,_,_,_,_,_,_,1):-resultado(libro(Tit,Autor,Gen,Precio,Fecha,Raiting,Estado,ISBN)),retract(resultado(libro(Tit,Autor,Gen,Precio,Fecha,Raiting,Estado,ISBN))),
    not((sub_string(Tit,_,_,_,Titulo))),
    asserta(resultado(libro(Tit,Autor,Gen,Precio,Fecha,Raiting,Estado,ISBN))),write(libro(Tit,Autor,Gen,Precio,Fecha,Raiting,Estado,ISBN)),nl,fail,!.

%Filtro Para restringir el Autor
nofiltro(_,Autor,_,_,_,_,_,_,2):-resultado(libro(Tit,Aut,Gen,Precio,Fecha,Raiting,Estado,ISBN)),retract(resultado(libro(Tit,Aut,Gen,Precio,Fecha,Raiting,Estado,ISBN))),
    not((sub_string(Aut,_,_,_,Autor))),
    asserta(resultado(libro(Tit,Aut,Gen,Precio,Fecha,Raiting,Estado,ISBN))),write(libro(Tit,Autor,Gen,Precio,Fecha,Raiting,Estado,ISBN)),nl,fail,!.


%Filtro para restringir el genero
nofiltro(_,_,Genero,_,_,_,_,_,3):-resultado(libro(Tit,Aut,Gen,Precio,Fecha,Raiting,Estado,ISBN)),retract(resultado(libro(Tit,Aut,Gen,Precio,Fecha,Raiting,Estado,ISBN))),
    not(pertenece(Genero,Gen)),
    asserta(resultado(libro(Tit,Aut,Gen,Precio,Fecha,Raiting,Estado,ISBN))),write(libro(Tit,Aut,Gen,Precio,Fecha,Raiting,Estado,ISBN)),nl,fail,!.
%Filtro para restringir el estado
nofiltro(_,_,_,_,_,_,Estado,_,4):-resultado(libro(Tit,Aut,Gen,Precio,Fecha,Raiting,Est,ISBN)),retract(resultado(libro(Tit,Aut,Gen,Precio,Fecha,Raiting,Est,ISBN))),
    not(Estado=Est),
    asserta(resultado(libro(Tit,Aut,Gen,Precio,Fecha,Raiting,Est,ISBN))),write(libro(Tit,Aut,Gen,Precio,Fecha,Raiting,Est,ISBN)),nl,fail,!.

%Calculo de cantidad de categorias de un libro
categoria(Cantidad):-resultado(libro(Titulo,Autor,Genero,Precio,Fecha,Raiting,Estado,ISBN)),retract(resultado(libro(Titulo,Autor,Genero,Precio,Fecha,Raiting,Estado,ISBN))),length(Genero,P),P>=Cantidad,asserta(resultado(libro(Titulo,Autor,Genero,Precio,Fecha,Raiting,Estado,ISBN))).

%Calculo de Dias
fecha(Dias):-
    get_time(T),
    stamp_date_time(T,date(Y,M,D,_,_,_,_,_,_),'UTC'),
    resultado(libro(Tit,Aut,Gen,Precio,Fecha,Raiting,Estado,ISBN)), retract(resultado(libro(Tit,Aut,Gen,Precio,Fecha,Raiting,Estado,ISBN))),date(Q,R,Z)=Fecha,
   ((((Z>=D)->Day is Z-D);((Z=<D)->Day is D-Z))),
   ((((R>=M)->Month is (R-M)*30);((R=<M)->Month is (M-R)*30))),
   ((((Q>=Y)->Year is (Q-Y)*365);((Q=<Y)->Year is (Y-Q)*365))),Total is Day+Month+Year,
   Total=<Dias,
   asserta(resultado(libro(Tit,Aut,Gen,Precio,Fecha,Raiting,Estado,ISBN))),fail,!.

combinacion(Resultado):-retractall(combinacion(X)).
% nofiltro(Titulo,Autor,Genero,Precio,Fecha,Raiting,Estado,ISBN,Resultado):-resultado(libro(Titulo,Autor,Genero,Precio,Fecha,Raiting,Estado,ISBN)),
%
    %(not(((Titulo=Tit)->sub_string(Tit,_,_,_,Titulo)))),
    %not(pertenece(Genero,Gen)),
    %(not((((Autor=Aut)->sub_string(Aut,_,_,_,Autor))))),
    %disponible(Dinero),Precio=<Dinero,Resultado=libro(Tit,Autor,Gen,Precio,Fecha,Raiting,Estado,ISBN),
    %write(Resultado),nl,fail.




% nofiltro(Titulo,Autor,Genero,Precio,Fecha,Raiting,Estado,ISBN):-resultado(libro(Tit,Aut,Gen,Precio,Fecha,Raiting,Est,ISBN)),retrac%t(resultado(libro(Tit,Aut,Gen,Precio,Fecha,Raiting,Est,ISBN))),not((sub_string(Tit,_,_,_,Titulo)));not((sub_string(Aut,_,_,_,Autor)));not(pertenece(Genero,Gen));not(Estado=Est),
%asserta(resultado(libro(Tit,Aut,Gen,Precio,Fecha,Raiting,Est,ISBN))),write(libro(Tit,Aut,Gen,Precio,Fecha,Raiting,Est,ISBN)),nl,fail,!.

% 1. Obtener un listado de libros que hayan salido hace menos de 15 dias
% y que su categoria sea fantasia epica y que tenga un rating de mas de 4
% estrellas.

% 2. Obtener listado de libros con mejor rating y que su precio sea menor
% de 600.

% 3. Obtener un listado de libros que en su categoria tengan viaje y que
% su rating sea mayor a 4 estrellas.

