const consoleEl = document.querySelector('.console-output');

function toggleActive(el, cls) {
    if (el instanceof HTMLElement && cls) {
        el.classList.toggle(cls);
    } else {
        console.error('Error in toggleActive');
    }
}

function gatherAllNames(listGroup) {
    const result = []
    listGroup.forEach((btn) => {
        if (btn.dataset.selected === 'True') {
            result.push(btn.textContent);
        }
    });
    return result;
}

function addOutput(message = '', color = 'white') {
    consoleEl.innerHTML += `<span style="color: ${color}">${message}</span><br>`;
    consoleEl.scrollTop = consoleEl.scrollHeight;
}

function selectListener(btn) {
    btn.addEventListener('click', () => {
        toggleActive(btn, 'active');
        if (btn.classList.contains('active')) {
            btn.dataset.selected = 'True';
            return;
        }
        btn.dataset.selected = 'False';
    });
}

/**
 *  Memorize data (names) in set (A or B)
 * @param {Array} names data
 * @param {Function} functionSet eel.memirezeA || eel.memorizeB
 */
async function memorize(names, functionSet) {
    if (names) {
        const someSet = await functionSet(names)();
        if(someSet) {
            addOutput(`Збережено! \n${someSet}`, 'green');
            return;
        }
        addOutput('Fatal error', 'red');
    }
    addOutput('Не обрано жодного імені', 'red');
}

export {toggleActive, gatherAllNames, addOutput, selectListener, memorize};
