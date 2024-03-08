const span = document.querySelector('#span');
const h1 = document.querySelector('#h1')
const div = document.querySelector('#message')

span.addEventListener('click', ()=>{
    div.parentNode.removeChild(div)
})

function autoCollapse() {
    if (div && h1) {
        setTimeout(() => {
            removeH1();
        }, 5000);
    }
}

function removeH1() {
    if (h1 && h1.parentNode === div) {
        div.parentNode.removeChild(div);
    }
}

autoCollapse();