<template>
  <div class="container">
    <div class="calculator">
      <div class="display">{{current || 0}}</div>
      <div @click="clear" class="btn operator basic">C</div>
      <div @click="sign" class="btn operator basic">+/-</div>
      <div @click="percent" class="btn operator basic">%</div>
      <div @click="divide" class="btn operator">/</div>
      <div class="btn operator">deg</div>
      <div @click="backspace" class="btn operator">&#x2190;</div>
      <div @click="append(7)" class="btn">7</div>
      <div @click="append(8)" class="btn">8</div>
      <div @click="append(9)" class="btn">9</div>
      <div @click="times" class="btn operator">*</div>
      <div class="btn operator">e<sup>x</sup></div>
      <div class="btn operator">sin</div>
      <div @click="append(4)" class="btn">4</div>
      <div @click="append(5)" class="btn">5</div>
      <div @click="append(6)" class="btn">6</div>
      <div @click="minus" class="btn operator">-</div>
      <div class="btn operator">x<sup>y</sup></div>
      <div class="btn operator">sinh</div>
      <div @click="append(1)" class="btn">1</div>
      <div @click="append(2)" class="btn">2</div>
      <div @click="append(3)" class="btn">3</div>
      <div @click="add" class="btn operator">+</div>
      <div class="btn operator">ln</div>
      <div class="btn operator">10<sup>x</sup></div>
      <div @click="dot" class="btn">.</div>
      <div @click="append(0)" class="zero btn">0</div>
      <div @click="equal" class="btn operator equal">=</div>
      <div @click="append('(')" class="btn operator">(</div>
      <div @click="append(')')" class="btn operator">)</div>
    </div>
  </div>
</template>

<script>
/* eslint-disable */
export default {
  name: 'Calculator',
  data () {
    return {
      previous: null,
      current: '',
      operator: null,
      operatorClicked: false
    }
  },
  methods: {
    clear () {
      this.current = ''
    },
    sign () {
      if (this.current !== '') {
        this.current = this.current.charAt(0) === '-'
          ? this.current.slice(1) : `-${this.current}`
      }
    },
    percent () {
      if (this.current !== '') {
        this.current = `${parseFloat(this.current) / 100}`
      }
    },
    append (number) {
      if (this.operatorClicked) {
        this.current = ''
        this.operatorClicked = false
      }
      this.current = `${this.current}${number}`
    },
    dot () {
      if (this.current.indexOf('.') === -1) {
        this.append('.')
      }
    },
    setPrevious () {
      this.previous = this.current
      this.operatorClicked = true
    },
    divide () {
      this.operator = (a, b) => Number(a / b)
      this.setPrevious()
    },
    times () {
      this.operator = (a, b) => Number(a * b)
      this.setPrevious()
    },
    minus () {
      this.operator = (a, b) => Number(b - a)
      this.setPrevious()
    },
    add () {
      this.operator = (a, b) => Number(a + b)
      this.setPrevious()
    },
    equal () {
      this.current = `${this.operator(
        parseFloat(this.current),
        parseFloat(this.previous)
      )}`
      this.previous = null
    },
    backspace () {
      this.current = this.current.slice(0, -1)
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
@import url("https://fonts.googleapis.com/css?family=Poppins:300,500&display=swap");

sup {
  font-size:x-small;
  vertical-align:super;
}

.calculator {
  display: grid;
  grid-template-rows: repeat(6, minmax(60px, auto));
  grid-template-columns: repeat(6, 60px);
  grid-gap: 12px;
  padding: 35px;
  font-family: "Poppins";
  font-weight: 300;
  font-size: 18px;
  background-color: #ffffff;
  border-radius: 15px;
  border: 2px solid #222;
}

.btn,
.zero {
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  text-align: center;
  text-decoration: none;
  outline: none;
  color: #484848;
  background-color: lightgrey;
  border-radius: 5px;
  -webkit-box-shadow: -1px 8px 8px 1px rgba(0, 0, 0, 0.75);
  -moz-box-shadow: -1px 8px 8px 1px rgba(0, 0, 0, 0.75);
  box-shadow: 0px 3px 3px 0px rgba(0, 0, 0, 0.75);
}

.display
{
  grid-column: 1 / 7;
  display: flex;
  align-items: center;
  font-weight: 500;
  color: #146080;
  border-bottom: 2px solid #e1e1e1;
  font-size: 55px;
  height: 65px;
  margin-bottom: 15px;
  background-color: #EEE;
}

.result {
  font-weight: 500;
  color: #146080;
  font-size: 55px;
  height: 65px;
}

.zero {
  grid-column: 2 / 4;
}

.equal {
  background-color: #0084ff !important;
  color: white !important;
}

.operator {
  background-color: rgb(255, 174, 0);
  color: white;
}

.basic {
  background-color: grey;
}
</style>
