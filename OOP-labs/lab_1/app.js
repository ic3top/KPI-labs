// C2 = 0 O1 = "+"
// C3 = 1 C = 1
// C5 = 3 O2 = "+"
// C7 = 5 тип індексів i та j = float

class Labochka {
  /**
     * @param {Number} n
     * @param {Number} a float
     * @param {Number} m
     * @param {Number} b float
     */
  constructor(a, n, b, m) {
    this.a = a;
    this.n = n;
    this.b = b;
    this.m = m;
  }

  calc() {
    /** @private */
    this._result = 0;

    if (this.a + 1 <= 0) {
      console.error('Division by zero');
      return;
    }

    for (let i = this.a; i <= this.n; i++) {
      for (let j = this.b; j <= this.m; j++) {
        this._result += (i + j) / (i + 1);
      }
    }
  }

  get result() {
    return this._result !== undefined ? this._result.toFixed(4) : 'No result!';
  }
}

const lb = new Labochka(3, 10, 123, 10);

console.log(lb.result);
lb.calc();
console.log(lb.result);
