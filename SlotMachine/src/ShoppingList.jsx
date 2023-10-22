function ShoppingList({ items }) {
  return (
    <>
      <ul>
        {items.map((i) => (
          <li>
            {i.name} - {i.quantity}
          </li>
        ))}
      </ul>
    </>
  );
}

export default ShoppingList;
