let s = document.querySelector('.menu');
let m = document.querySelector('.menux');
let list = document.querySelector('ul');
m.style.display = "none";
s.addEventListener('click', clickon);
		
function clickon(){
	s.style.display ="none";
	m.style.display ="block";
	list.style.display ="block";
};
		
m.addEventListener('click', clickoff);
		
function clickoff(){
	s.style.display ="block";
	m.style.display ="none";
	list.style.display ="none";
};