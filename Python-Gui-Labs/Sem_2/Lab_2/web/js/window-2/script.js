const consoleEl = document.querySelector('.console-output');
const containerS_A = document.querySelector('#s-A');
const containerS_B = document.querySelector('#s-B');
const containerR_A = document.querySelector('#r-A');
const containerR_B = document.querySelector('#r-B');

const arrowsDrawerR = $cArrows('#r-relative', {render: {strokeStyle: '#949494', shadowColor: '#000000', shadowBlur: 3, lineWidth: 1 }, base: {canvasZIndex: '1'},});
const arrowsDrawerS = $cArrows('#s-relative', {render: {strokeStyle: '#949494', shadowColor: '#000000', shadowBlur: 3, lineWidth: 1 }, base: {canvasZIndex: '1'},});

const generateHex = () => '#' + Math.random().toString(16).substr(-6);

eel.get_A()(([arr, setName]) => consoleEl.innerHTML += generateList(arr, setName));
eel.get_B()(([arr, setName]) => consoleEl.innerHTML += generateList(arr, setName));

function generateList(someArr=  [], setName = 'Множина: ') {
    let fragment = `${setName}: <br>`;
    someArr.forEach(([index, name]) => {
        const li = `${index}) ${name}<br>`;
        fragment += (li);
    });

    return fragment === `${setName}: <br>` ? '' : fragment;
}


function cardTemplate(name, relName, setName) {
    return `<div class="card text-center shadow-1-strong"><div class="card-header" data-id="${relName}-${setName}-${name}">${name}</div></div>`;
}

function initData(data) {
    console.log(data);
    namesA = data.A;
    namesB = data.B;

    namesA.forEach((name) => {
        containerS_A.innerHTML += cardTemplate(name, 's', 'a');
        containerR_A.innerHTML += cardTemplate(name, 'r', 'a');
    });

    namesB.forEach((name) => {
        containerS_B.innerHTML += cardTemplate(name, 's', 'b');
        containerR_B.innerHTML += cardTemplate(name, 'r', 'b');
    });
}

function drawArrow(drawer, firstSelector, secSelector) {
    drawer.arrow(firstSelector, secSelector, {
        arrow: {
            connectionType: 'side',
            sideFrom: 'bottom',
            sideTo: 'top'
        }, render: {strokeStyle: `${generateHex()}`}
    });
}

function createR(data) {
    (data.A).forEach((name) => {
        if (data[name]) {
            if (isWomen(data[name][0])) {
                console.error(`Error in createR func. ${data[name][0]} - is a women`);
                return;
            }
            drawArrow(arrowsDrawerR, `[data-id="r-a-${name}"]`, `[data-id="r-b-${data[name][0]}"]`);
        }
    })
}

function createS(data) {
    (data.A).forEach((name) => {
        if (data[name]) {
            drawArrow(arrowsDrawerS, `[data-id="s-a-${name}"]`, `[data-id="s-b-${data[name][1]}"]`);
        }
    })
}

function isWomen(name) {
    const last = name.split('').pop()

    return last === 'а' || last === 'я';
}

eel.createRelative()((data) => {
    initData(data);
    createR(data);
    createS(data);
});
