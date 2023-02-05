const container = document.querySelector('#container');
const content = document.createElement('p');
const content2 = document.createElement('h3');
const content3 = document.createElement('div');

const btn = document.querySelector('#btn');
btn.addEventListener('click', () => {
    alert("Hello World");
  });


content3.classList.add('content');
content2.classList.add('content');
content2.textContent='Hey Im red!';
content.classList.add('content');
content.textContent='I’m a blue h3!';
container.appendChild(content);
container.appendChild(content2);
container.appendChild(content3);

content3.element.add('p')
content3.element.add('h1')
content3.element.textContent='Im a div';


content.style.cssText = 'color: red; background: white;';
content.style.cssText = 'color: blue;'
content.style.csstext = ' border: black; background: pink;'

