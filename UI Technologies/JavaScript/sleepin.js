function sleepIn(weekday, vaccation){
  if (weekday == false){
    return true
  }
  else if (vaccation == true){
    return true
  }
  return false
}

console.log("Is employee Sleeping: " + sleepIn(true, true))
console.log("Is employee Sleeping: " + sleepIn(true, false))
console.log("Is employee Sleeping: " + sleepIn(false, true))
console.log("Is employee Sleeping: " + sleepIn(false, false))
