const eliminarBtns = document.querySelectorAll("#eliminar");
eliminarBtns.forEach(eliminar=>{
    eliminar.addEventListener("click", (event)=>{
        confirmar = window.confirm("¿Realmente deseas eliminar este producto?");
        if(confirmar){
            
        } else {
            event.preventDefault();
        }
    })
})