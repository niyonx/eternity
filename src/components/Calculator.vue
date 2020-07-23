<template>
  <div class="calculator">
    <div class="calculator-bar">
      ETERNITY SCIENTIFIC CALCULATOR
    </div>
    <div class="calculator-display">{{expression || 0}}</div>

    <div class="calculator-keys">
      <div class="row">
        <button class="calculator-btn" @click="appendOp('sin(')">sin</button>
        <button class="calculator-btn" @click="appendOp('tenPower(')">10<sup>x</sup></button>
        <button class="calculator-btn" @click="appendOp('MAD(')">MAD</button>
        <button class="calculator-btn" @click="appendOp('σ(')">σ</button>
      </div>

      <div class="row">
        <button class="calculator-btn" @click="appendOp('ePower(')">e<sup>x</sup></button>
        <button class="calculator-btn" @click="appendOp('power(')">x<sup>y</sup></button>
        <button class="calculator-btn" @click="appendNum('e')">e</button>
        <button class="calculator-btn" @click="appendNum('π')">π</button>
      </div>
      <div class="row">
        <button class="calculator-btn" @click="changeAngleMode">{{angleMode}}</button>
        <button class="calculator-btn" @click="appendOp(',')">,</button>
        <button class="calculator-btn" @click="appendNum('(')">(</button>
        <button class="calculator-btn" @click="appendNum(')')">)</button>
      </div>
      <div class="row">
        <button class="calculator-btn" @click="appendOp('*')">*</button>
        <button class="calculator-btn" @click="appendOp('/')">/</button>
        <button class="calculator-btn" @click="backspace">←</button>
        <button class="calculator-btn" @click="clear">C</button>
      </div>
      <div class="row">
        <button class="calculator-btn num-btn" @click="appendNum('7')">7</button>
        <button class="calculator-btn num-btn" @click="appendNum('8')">8</button>
        <button class="calculator-btn num-btn" @click="appendNum('9')">9</button>
        <button class="calculator-btn" @click="appendOp('-')">-</button>
      </div>
      <div class="row">
        <button class="calculator-btn num-btn" @click="appendNum('4')">4</button>
        <button class="calculator-btn num-btn" @click="appendNum('5')">5</button>
        <button class="calculator-btn num-btn" @click="appendNum('6')">6</button>
        <button class="calculator-btn" @click="appendOp('+')">+</button>
      </div>
      <div class="row">
        <button class="calculator-btn num-btn " @click="appendNum('1')">1</button>
        <button class="calculator-btn num-btn " @click="appendNum('2')">2</button>
        <button class="calculator-btn num-btn " @click="appendNum('3')">3</button>
        <button class="calculator-btn" @click="appendNum(ans)">Ans</button>
      </div>
      <div class="row">
        <button class="calculator-btn num-btn" @click="appendNum('-')">+/-</button>
        <button class="calculator-btn num-btn" @click="appendNum('0')">0</button>
        <button class="calculator-btn num-btn" @click="appendNum('.')">.</button>
        <button class="calculator-btn eq-btn" @click="equal">=</button>
        <!-- <button class="calculator-btn notshow"></button> -->
      </div>
    </div>
  </div>
</template>

<script>
// import MathTool from '../utils/MathTool'
import $backend from '../backend'

/* eslint-disable */
  export default {
    name: 'Calculator',
    data () {
      return {
        expression: '',
        angleMode: 'deg',
        resources: [],
        error: '',
        ans: ''
      }
    },
    methods: {
      clear () {
        this.expression = ''
      },
      backspace () {
        if (typeof this.expression === typeof 1) {
          this.expression = ''
        } else {
          this.expression = this.expression.toString().slice(0, -1)
        }
      },
      appendNum (e) {
        if (typeof this.expression === typeof 1) {
          this.expression = e
        } else {
          this.expression += e
        }
      },
      appendOp (e) {
          this.expression += e
      },
      equal () {
        $backend.evaluate(this.expression, this.angleMode)
          .then(responseData => {
            this.expression = responseData;
            this.ans = this.expression
          }).catch(error => {
            console.log(error)
            this.error = error.message
            this.expression = 'Syntax Error'
          })
      },
      changeAngleMode () {
        if (this.angleMode === 'deg') {
          this.angleMode = 'rad'
        } else {
          this.angleMode = 'deg'
        }
      },
      fetchResource () {
        $backend.fetchResource()
          .then(responseData => {
            this.resources.push(responseData)
          }).catch(error => {
            this.error = error.message
          })
      },
      fetchSecureResource () {
        $backend.fetchSecureResource()
          .then(responseData => {
            this.resources.push(responseData)
          }).catch(error => {
            this.error = error.message
          })
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  /*@import url("https://fonts.googleapis.com/css?family=Poppins:300,500&display=swap");*/

  .calculator {
    background: #2E3A52;
    flex: 1;
    padding: 10px;
    margin: 10px;
    color: white;
    border-radius: 10px;
    box-shadow: 0 4px 6px 1px rgba(0, 0, 0, 0.6);
    position: relative;
    min-width: 280px;
    max-width: 480px;
  }

  .calculator-bar {
    text-align: center;
    font-size: 0.9rem;
  }

  .calculator-display {
    font-size: 2rem;
    height: 100px;
    padding: 0 10px;
    background-color: #2E3A52;
    color: #fff;
    display: flex;
    align-items: center;
    justify-content: flex-end;
    overflow: hidden;
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
    /*height: 110px;*/
    background-color: #19D5A3;
    color: #212C42
  }

  .calculator-keys .row .calculator-btn.num-btn {
    color: #fff
  }
</style>
