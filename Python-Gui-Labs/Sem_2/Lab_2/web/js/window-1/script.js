import {addOutput, gatherAllNames, selectListener, memorize} from './utils.js';

// UI elements
const listGroupMen = document.getElementById('group-men').querySelectorAll('button');
const listGroupWomen = document.getElementById('group-women').querySelectorAll('button');

const menSelector = document.getElementById('write-men');
const saveMen = document.getElementById('save-men');

const womenSelector = document.getElementById('write-women');
const saveWomen = document.getElementById('save-women');

const clearA = document.getElementById('clear-A');
const clearB = document.getElementById('clear-B');

const writeA = document.getElementById('write-A');
const writeB = document.getElementById('write-B');

const readA = document.getElementById('read-A');
const readB = document.getElementById('read-B');

// Listeners
listGroupMen.forEach(selectListener);

listGroupWomen.forEach(selectListener);

saveMen.addEventListener('click', () => {
    if (menSelector.value === 'A') {
        const names = gatherAllNames(listGroupMen);
        memorize(names, eel.memorizeA);
        return;
    }

    if (menSelector.value === 'B') {
        const names = gatherAllNames(listGroupMen);
        memorize(names, eel.memorizeB);
        return;
    }
    addOutput('Необрано множину', 'red');
});

saveWomen.addEventListener('click', () => {
    if (womenSelector.value === 'A') {
        const names = gatherAllNames(listGroupWomen);
        memorize(names, eel.memorizeA);
        return;
    }

    if (womenSelector.value === 'B') {
        const names = gatherAllNames(listGroupWomen);
        memorize(names, eel.memorizeB);
        return;
    }
    addOutput('Необрано множину', 'red');
});

clearA.addEventListener('click', () => {
    if (confirm('Множина A буде очищена.')) {
        eel.clear('A')(addOutput);
    }
});
clearB.addEventListener('click', () => {
    if (confirm('Множина B буде очищена.')) {
        eel.clear('B')(addOutput);
    }
});

writeA.addEventListener('click', () => eel.writeA()(addOutput));
writeB.addEventListener('click', () => eel.writeB()(addOutput));

readA.addEventListener('click', () => eel.readA()(addOutput));
readB.addEventListener('click', () => eel.readB()(addOutput));
