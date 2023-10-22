import { useState } from "react";
import "./App.css";
import Slot from "./Slot";
import ShoppingList from "./ShoppingList";

const items = [
  {
    name: "Chocolate",
    quantity: 1,
    isDone: true,
  },
  {
    name: "Milk",
    quantity: 2,
    isDone: false,
  },
  {
    name: "Egg",
    quantity: 12,
    isDone: true,
  },
];

function App() {
  return (
    <>
      <ShoppingList items={items} />
      {/* // <Slot val1={"d"} val2={"d"} val3={"d"} />; */}
    </>
  );
}

export default App;
