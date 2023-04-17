
var nombre = "victor"
var altura = 180;

var concatenacion = nombre + " " + altura;



if(altura >= 190){
    datos.innerHTML += '<h1>eres una alta</h1>';
}else{
    datos.innerHTML += '<h1>eres bajo</h1>'
}

/*
for(var i = 2000; i<=2020; i++){
    //bloque
    datos.innerHTML += "<h2>estasmos en el año: " +i;
}
*/

function MustramiNombre(nombre, altura){
    var datos = document.getElementById("datos");
datos.innerHTML = `
    <h1>hola soy la caja</h1>
    <h2>mi nombre es ${nombre}</h2>
    <h3>mido ${altura}</h3>
`;
}

function imprimir(){
    
}

MustramiNombre("victor  HH", 190);

