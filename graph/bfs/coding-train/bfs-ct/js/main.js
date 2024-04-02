var data;
var graph;
var dropdown
function preload() {
  data = loadJSON("./js/kevinbacon.json");
}

function setup() {
  noCanvas();
  graph = new Graph();
  dropdown = createSelect();
  dropdown.changed(bfs)
  var movies = data.movies;

  for (var i = 0; i < movies.length; i++) {
    var movie = movies[i].title;
    var cast = movies[i].cast;
    var movieNode = new Node(movie);
    graph.addNode(movieNode)

    for (var j = 0; j < cast.length; j++) {
      var actor = cast[j];
      var actorNode = graph.getNode(actor);
      if (actorNode == undefined) {
        actorNode = new Node(actor);
        dropdown.option(actor);
      }
      graph.addNode(actorNode);
      movieNode.addEdge(actorNode);
    }
  }
};

function bfs() {
  var start = graph.setStart(dropdown.value());
  console.log(start)
  var end = graph.setEnd("Kevin Bacon");

  var queue = [];

  start.searched = true;
  queue.push(start);
  while (queue.length > 0) {
    var current = queue.shift();
    if (current == end) {
      console.log("Found! " + current.value);
      break;
    }
    var edges = current.edges;
    for (var i = 0; i < edges.length; i++) {
      var neighbour = edges[i];
      if (!neighbour.searched) {
        neighbour.searched = true;
        neighbour.parent = current;
        queue.push(neighbour);
      }
    }

  }
  var path = [];
  path.push(end);
  var next = end.parent;
  end.parent = null
  end.searched = false
  while (next != null) {
    path.push(next);
    temp = next;
    next = next.parent;
    temp.parent = null
    temp.searched = false
  }
  path.reverse();
  var txt = '';
  for (var i = 0; i < path.length - 1; i++) {
    var n = path[i];
    txt += `${n.value} -->`
  }
  txt += path[path.length - 1].value;
  createP(txt);

}
function draw() {
  background(255);
  circle(100, 100, 100);
}

function windowResized() {
  resizeCanvas(windowWidth, windowHeight);
}
