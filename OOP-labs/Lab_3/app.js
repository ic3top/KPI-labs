// C3 = 1 | C = StringBuffer - provides string mutability
// C17 = 4
// В кожному реченні заданого тексту змінити
// місцями перше та останнє слово, не змінивши довжини речення.
// String object unchangable in JAVA
function isString(variable) {
  return typeof (variable) === 'string';
}

class Text {
  constructor(str) {
    if (isString(str)) {
      this.str = str;
      // eslint-disable-next-line no-useless-escape
      this.arr = this.str.replace(/[0-9]|[.,\/#!$%?\^&\*;:{}=\-_`~()]/g, ' ').trim().split(' ');
    } else {
      throw new Error('Not a string');
    }
  }

  move() {
    if (this.arr.length < 2) {
      console.error('Less than two words');
      return;
    }
    const lastEl = this.arr[this.arr.length - 1];
    const firstEl = this.arr[0];
    // replace - replaces only first occurence
    this.replaced = this.str.replace(lastEl, firstEl).replace(firstEl, lastEl);
  }
}

Text.prototype.someStuff = 'something!';
Text.someStuff = 'something! Class';

const newStr = new Text(' -_-?1,2,3 First  ,.  New sentence second ,third, LastWordInThisFckSpeech!   ');
newStr.move();
console.log(newStr.replaced);
