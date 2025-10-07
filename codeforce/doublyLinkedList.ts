type Node<T> = {
  value: T;
  prev?: Node<T>;
  next?: Node<T>;
};

export default class DoublyLinkedList<T> {
  public length: number;
  private head?: Node<T>;
  private tail?: Node<T>;
  constructor() {
    this.head = undefined;
    this.tail = undefined;
    this.length = 0;
  }

  prepend(item: T) {
    const node = { value: item } as Node<T>;
    this.length++;
    if (!this.head) {
      this.head = this.tail = node;
      return;
    }
    node.next = this.head;
    this.head.prev = node;
    this.head = node;
  }
  append(item: T) {
    const node = { value: item } as Node<T>;
    this.length++;
    if (!this.tail) {
      this.tail = this.head = node;
      return;
    }
    node.prev = this.tail;
    this.tail.next = node;
    this.tail = node;
  }
  insertAt(item: T, idx: number) {
    if (idx == 0) {
      this.prepend(item);
      return;
    }
    if (idx == this.length) {
      this.append(item);
      return;
    }
    const node = { value: item } as Node<T>;
    this.length++;
    let curr = this.head;
    for (let i = 0; curr && i < idx; i++) {
      curr = curr.next;
    }
    if (!curr) {
      throw new Error("ops not that found that position");
    }
    node.next = curr;
    node.prev = curr.prev;
    if (curr.prev) {
      curr.prev.next = node;
    }
    curr.prev = node;
  }
}
