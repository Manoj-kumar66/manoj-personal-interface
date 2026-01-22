function startup(){
document.getElementById("bootSound").play();
typeText("INITIALIZING MANOJ AI SYSTEM...");
network();
hologram();
}

/* TYPING EFFECT */
function typeText(text){
let i=0;
let el=document.getElementById("typing");
let interval=setInterval(()=>{
el.textContent+=text[i];
i++;
if(i>=text.length)clearInterval(interval);
},60);
}

/* NETWORK BACKGROUND */
function network(){
const canvas=document.getElementById("bg");
const c=canvas.getContext("2d");
canvas.width=innerWidth;
canvas.height=innerHeight;

let points=[];
for(let i=0;i<80;i++)
points.push({x:Math.random()*canvas.width,y:Math.random()*canvas.height,vx:1-Math.random()*2,vy:1-Math.random()*2});

function draw(){
c.clearRect(0,0,canvas.width,canvas.height);
points.forEach(p=>{
p.x+=p.vx;
p.y+=p.vy;
if(p.x<0||p.x>canvas.width)p.vx*=-1;
if(p.y<0||p.y>canvas.height)p.vy*=-1;
c.fillStyle="#00f6ff";
c.fillRect(p.x,p.y,2,2);
});
requestAnimationFrame(draw);
}
draw();
}

/* 3D HOLOGRAM */
function hologram(){
const scene=new THREE.Scene();
const camera=new THREE.PerspectiveCamera(75,1,0.1,1000);
const renderer=new THREE.WebGLRenderer({alpha:true});
renderer.setSize(200,200);
document.getElementById("holo").appendChild(renderer.domElement);

const geo=new THREE.IcosahedronGeometry(1,1);
const mat=new THREE.MeshBasicMaterial({color:0x00f6ff,wireframe:true});
const mesh=new THREE.Mesh(geo,mat);
scene.add(mesh);
camera.position.z=3;

function animate(){
mesh.rotation.x+=0.01;
mesh.rotation.y+=0.01;
renderer.render(scene,camera);
requestAnimationFrame(animate);
}
animate();
}

