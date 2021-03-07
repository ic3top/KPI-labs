const union = d3.select("#union");
const cross = d3.select("#cross");
const difference = d3.select("#difference");
const addition = d3.select("#addition");
const resInverse = document.querySelector("#inverse .result");
const resUnion = document.querySelector("#union .result");
const resDifference = document.querySelector('#difference .result');
const resCross = document.querySelector("#cross .result");
const resAddition = document.querySelector("#addition .result");

const sets = [ {sets: ["S"], size: 6},
             {sets: ["R"], size: 6},
             {sets: ["S","R"], size: 1}];

const uSets = [ {sets: ["U"], size: 6},
              {sets: ["R"], size: 1},
              {sets: ["U","R"], size: 1}];

const chart = venn.VennDiagram().width(400).height(300);

function initData(el, data) {
    try {
        if (!data.length) {
            el.innerHTML += '{}';
            return;
        }
        el.innerHTML += '{'
        data.forEach((arr) => {
            el.innerHTML += `(${arr}), `
        });
        el.innerHTML = el.innerHTML.slice(0, -2) + '}';
    } catch(e) {
        console.error(e + " in initData func");
    }
}
function paintBlue(selector) {
    selector.style("fill", "#42A5F5").style("fill-opacity", 1);
}

function paintBlack(selector) {
    selector.style("fill", "#5e5554").style("fill-opacity", 1);
}

union.datum(sets).call(chart);
paintBlue(union.selectAll(".venn-circle path"));

cross.datum(sets).call(chart);
paintBlack(cross.selectAll(".venn-circle path"));
paintBlue(cross.selectAll(".venn-area.venn-intersection path"));

difference.datum(sets).call(chart);
paintBlue(difference.select('[data-venn-sets="R"] path'));
paintBlack(difference.select('[data-venn-sets="S"] path'));
paintBlack(difference.selectAll(".venn-area.venn-intersection path"));

addition.datum(uSets).call(chart);
paintBlue(addition.select('[data-venn-sets="U"] path'));
paintBlack(addition.select('[data-venn-sets="R"] path'));

eel.getRelative()((data) => console.log(data));

eel.union()((data) => {
    initData(resUnion, data);
});
eel.cross()((data) => {
    initData(resCross, data);
})
eel.difference()((data) => {
    initData(resDifference, data);
});
eel.addition()((data) => {
    initData(resAddition, data);
});
eel.inverse()((data) => {
    initData(resInverse, data);
});