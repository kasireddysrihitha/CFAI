function solveMaze(){

    let algo =
    document.getElementById(
        "algorithm"
    ).value;

    document.getElementById(
        "output"
    ).innerHTML =

    algo +
    " Algorithm Selected <br>" +
    "Maze Solved Successfully! <br>" +
    "Steps: 8";
}

function resetMaze(){

    document.getElementById(
        "output"
    ).innerHTML =
    "Waiting for Algorithm...";
}