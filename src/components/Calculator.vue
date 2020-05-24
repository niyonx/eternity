<template>

  <div class="calculator">
    <div class="calculator-bar">
      ETERNITY CALCULATOR
    </div>
    <div class="calculator-display">{{expression || 0}}</div>

    <div class="calculator-keys">
      <div class="row">
        <button class="calculator-btn" @click="append('sin(')">sin</button>
        <button class="calculator-btn" @click="append('sinh(')">sinh</button>
        <button class="calculator-btn" @click="append('ln(')">ln</button>
        <button class="calculator-btn" @click="append('10power(')">10<sup>x</sup></button>
      </div>

      <div class="row">
        <button class="calculator-btn" @click="append('epower(')">e<sup>x</sup></button>
        <button class="calculator-btn" @click="append('power(')">x<sup>y</sup></button>
        <button class="calculator-btn" @click="append('e')">e</button>
        <button class="calculator-btn" @click="append('π')">π</button>
      </div>
      <div class="row">
        <button class="calculator-btn" @click="append('%')">%</button>
        <button class="calculator-btn" @click="append('deg')">deg</button>
        <button class="calculator-btn" @click="append('(')">(</button>
        <button class="calculator-btn" @click="append(')')">)</button>
      </div>
      <div class="row">
        <button class="calculator-btn" @click="append('*')">*</button>
        <button class="calculator-btn" @click="append('/')">/</button>
        <button class="calculator-btn" @click="backspace">←</button>
        <button class="calculator-btn" @click="clear">C</button>
      </div>
      <div class="row">
        <button class="calculator-btn num-btn" @click="append('7')">7</button>
        <button class="calculator-btn num-btn" @click="append('8')">8</button>
        <button class="calculator-btn num-btn" @click="append('9')">9</button>
        <button class="calculator-btn" @click="append('-')">-</button>
      </div>
      <div class="row">
        <button class="calculator-btn num-btn" @click="append('4')">4</button>
        <button class="calculator-btn num-btn" @click="append('5')">5</button>
        <button class="calculator-btn num-btn" @click="append('6')">6</button>
        <button class="calculator-btn" @click="append('+')">+</button>
      </div>
      <div class="row">
        <button class="calculator-btn num-btn " @click="append('1')">1</button>
        <button class="calculator-btn num-btn " @click="append('2')">2</button>
        <button class="calculator-btn num-btn " @click="append('3')">3</button>
        <button class="calculator-btn eq-btn" @click="equal">=</button>
      </div>
      <div class="row">
        <button class="calculator-btn num-btn" @click="append('-')">+/-</button>
        <button class="calculator-btn num-btn" @click="append('0')">0</button>
        <button class="calculator-btn num-btn" @click="append('.')">.</button>
        <button class="calculator-btn notshow"></button>
      </div>
    </div>
  </div>
</template>

<script>
/* eslint-disable */
  export default {
    name: 'Calculator',
    data () {
      return {
        expression: ''
      }
    },
    methods: {
      clear () {
        this.expression = ''
      },
      backspace () {
        this.expression = this.expression.slice(0, -1)
      },
      append (e) {
        this.expression += e
      },
      equal(){

      }

    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  /*@import url("https://fonts.googleapis.com/css?family=Poppins:300,500&display=swap");*/

  html,
  body {
    margin: 0;
    padding: 0;
    height: 100%;
  }

  /*Use media query for rem*/
  @media (min-width: 320px) {
    html {
      font-size: 14px;
    }
  }

  @media (min-width: 375px) {
    html {
      font-size: 16px;
    }
  }

  @media (min-width: 440px) {
    html {
      font-size: 18px;
    }
  }

  body {
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: #ccc;
  }

  .calculator {
    background: #2E3A52;
    flex: 1;
    padding: 10px;
    margin: 10px;
    color: white;
    border-radius: 10px;
    box-shadow: 0 4px 6px 0.2px rgba(0, 0, 0, 0.6);
    position: relative;
    min-width: 280px;
    max-width: 480px;
  }

  .calculator-bar {
    text-align: center;
    font-size: 0.9rem;
  }

  .calculator-display {
    font-size: 2.5rem;
    height: 100px;
    padding: 0 10px;
    background-color: #2E3A52;
    color: #fff;
    display: flex;
    align-items: center;
    justify-content: flex-end;
    overflow: hidden;
  }

  .calculator-keys {
  }

  .calculator-keys .row {
    display: flex;
    height: 60px;
  }

  .calculator-keys .row .calculator-btn {
    cursor: pointer;
    flex: 1;
    padding: 5px;
    margin: 5px;
    height: 50px;
    font-size: 1.3rem;
    border: none;
    background-color: #212C42;
    border-radius: 7px;
    transition: color .15s ease-in-out, background-color .15s ease-in-out, border-color .15s ease-in-out, box-shadow .15s ease-in-out;
    color: #19D5A3
  }

  .calculator-keys .row .calculator-btn.notshow {
    visibility: hidden;
  }

  .calculator-keys .row .calculator-btn.eq-btn {
    position: relative;
    top: 0;
    left: 0;
    height: 110px;
    background-color: #19D5A3;
    color: #212C42
  }

  .calculator-keys .row .calculator-btn.num-btn {
    color: #fff
  }
</style>
