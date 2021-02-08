// C11 = 10 Визначити клас студент, який складається як мінімум з 5-и полів.
// private fields - 66%
// static class fields - 70%

/** Class representing a student. */
class Student {
  /** @private */
  #scholarship;
  /**
   * Create a student.
   * @param {String} name
   * @param {String} surName
   * @param {Number} scholarship
   * @param {number} rating  rating in the group.
   * @param {String} group
   */
  constructor(name, surName, scholarship, rating, group) {
    this.name = name;
    this.surName = surName;
    this.university = 'KPI';
    this.#scholarship = scholarship;
    this.rating = rating;
    this.group = group;
  }
  /**
   * get the scholarship value.
   * @return {number} The scolarship value.
   */
  getScolarship() {
    return this.#scholarship;
  }

  toString() {
    return `${this.name} ${this.surName} in the ${this.group} group`;
  }
}

const st1 = new Student('Igoryok', 'Ivanov', 1300, 23, 'KI-13');
const st2 = new Student('Peter', 'Trembita', 1600, 123, 'SFT-05');
const st3 = new Student('Jack', 'Gyzyl', 1800, 56, 'FT-90');
const st4 = new Student('Ann', 'Itakova', 2800, 2, 'PK-23');
const st5 = new Student('John', 'Idk', 800, 48, 'HT-42');

class Main {
    static arr = [st1, st2, st3, st4, st5];
    /** Sorts in order of growth by scholarships */
    static #sortByScl(studentPrev, studentNext) {
      return studentNext.getScolarship() - studentPrev.getScolarship();
    }
    /** Sorts in order of decline by rating */
    static #sortByRating(studentPrev, studentNext) {
      return studentPrev.rating - studentNext.rating;
    }

    /**
     * Sorts an array by scholarship.
     * @returns {(Array)} An array that contains sorted students by scholarship.
     */
    static getSortedScl() {
      return Main.arr.sort(Main.#sortByScl); 
    }

    /**
     * Sorts an array by rating.
     * @returns {(Array)} An array that contains sorted students by rating.
     */
    static getSortedRat() {
      return Main.arr.sort(Main.#sortByRating)
    }
}

console.log(st1);
console.log(Main.getSortedRat());