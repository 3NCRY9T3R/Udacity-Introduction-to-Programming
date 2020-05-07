function changeColor() {
    const color = document.getElementById("colorPicker").value;
    this.style.background = color;
}

function makeGrid() {
    const height = document.getElementById("input_height").value;
    const width = document.getElementById("input_width").value;
    const base = document.getElementById("pixel_canvas");
    base.innerText=""; //empty default table

    for (let h=0; h<height; ++h) {
        const row = base.insertRow(-1); //adding new column
        for (let w=0; w<width; ++w) {
            const cell = row.insertCell(-1); //adding new row
            cell.onclick = changeColor; //onclick event handler
        }
    }
    event.preventDefault(); //default
}
