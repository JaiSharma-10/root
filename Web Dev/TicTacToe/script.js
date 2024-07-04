const X_CLASS = 'x'
const CIRCLE_CLASS = 'circle'
const Winning_Combination = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]

]
const cellElement = document.querySelectorAll('[data-cell]')
const Board = document.getElementById('board')
const winningMessageElement = document.getElementById('winningMessage')
const restartButton = document.getElementById('restart-button')
const winningMessageTextElement = document.querySelector('[data-winning-message-text]')

let circleTurn
//access to all the cell element in boards
restartButton.addEventListener('click', startGame)


startGame()


function startGame() {
    circleTurn=false
    cellElement.forEach(cell => {
        cell.classList.remove(X_CLASS)
        cell.classList.remove(CIRCLE_CLASS)
        cell.removeEventListener('click', handleClick)
        cell.addEventListener('click', handleClick, { once: true })
    })//handle click of the cell onces
    setBoardHoverClass()
    winningMessageElement.classList.remove('show')
}


function handleClick(e) {
    //console.log('clicked')
    //Check for Draw
    
    const cell = e.target //get cell
    const currentClass = circleTurn ? CIRCLE_CLASS : X_CLASS
    //placeMark
    placeMark(cell, currentClass)
     //Check for Win
    if (checkWin(currentClass)) {
        endGame(false)
    }
    else if (isDraw()) {
        endGame(true)
    }
    else {
        //Switch turn
        swapTurns()
        setBoardHoverClass()
    }
    


}

function endGame(draw) {
    if (draw) {
        winningMessageTextElement.innerText = 'Draw!'
    }
    else {
        winningMessageTextElement.innerText = `${circleTurn ? "O's" :
           "X's" } Wins!`
    }
    winningMessageElement.classList.add('show')
}

function isDraw() {
    return [...cellElement].every(cell => {
        return cell.classList.contains(X_CLASS) || cell.classList.contains(CIRCLE_CLASS)
    })
}

function placeMark(cell, currentClass) { 
    cell.classList.add(currentClass)
}

function swapTurns() {
    circleTurn = !circleTurn
}

function setBoardHoverClass() {
    Board.classList.remove(X_CLASS)
    Board.classList.remove(CIRCLE_CLASS)
    if (circleTurn) {
        Board.classList.add(CIRCLE_CLASS)
    }
    else {
        Board.classList.add(X_CLASS)

    }

}

function checkWin(currentClass) {
    return Winning_Combination.some(combination => {
        return combination.every(index => {
            return cellElement[index].classList.contains(currentClass)
        })
    })
}
