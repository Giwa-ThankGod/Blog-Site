let s = document.querySelector('.burger-close');
let m = document.querySelector('.burger');
let list = document.querySelector('ul');
s.style.display = "none";
m.addEventListener('click', clickon);
		
function clickon(){
	m.style.display ="none";
	s.style.display ="block";
	list.style.display ="block";
};
		
s.addEventListener('click', clickoff);
		
function clickoff(){
	m.style.display ="block";
	s.style.display ="none";
	list.style.display ="none";
};