<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Books</h1>
        <AlertPath :message="message" v-if="showMessage" />
        <hr /><br /><br />
        <router-link
          :to="{ path: '/books/addbook' }"
          type="button"
          class="btn btn-success btn-sm"
          @click="toggleAddBookModal"
        >
          Add Book
        </router-link>
        <br /><br />
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Title</th>
              <th scope="col">Author</th>
              <th scope="col">Read?</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(book, index) in paginatedBooks" :key="index">
              <td>{{ book.title }}</td>
              <td>{{ book.author }}</td>
              <td>
                <span v-if="book.read">Yes</span>
                <span v-else>No</span>
              </td>
              <td>
                <div class="btn-group" role="group">
                  <router-link
                    :to="{ path: '/books/update' }"
                    type="button"
                    class="btn btn-warning btn-sm"
                    @click="toggleEditBookModal(book)"
                  >
                    Update
                  </router-link>
                  <router-link
                    :to="{ path: '/books/delete' }"
                    type="button"
                    class="btn btn-danger btn-sm"
                    @click="handleDeleteBook(book)"
                  >
                    Delete
                  </router-link>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- add new book modal -->
    <div
      ref="addBookModal"
      class="modal fade"
      :class="{ show: activeAddBookModal, 'd-block': activeAddBookModal }"
      tabindex="-1"
      role="dialog"
    >
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Add Book</h5>
            <button type="button" class="close" @click="toggleAddBookModal">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <form>
              <div class="form-group">
                <label for="addBookTitle">Title</label>
                <input
                  type="text"
                  class="form-control"
                  id="addBookTitle"
                  v-model="addBookForm.title"
                />
                <div v-if="!addBookForm.title && addBookForm.titleTouched" class="text-danger">Title is required</div>
              </div>
              <div class="form-group">
                <label for="addBookAuthor">Author</label>
                <input
                  type="text"
                  class="form-control"
                  id="addBookAuthor"
                  v-model="addBookForm.author"
                />
                <div v-if="!addBookForm.author && addBookForm.authorTouched" class="text-danger">Author is required</div>
              </div>
              <div class="form-group">
                <div class="form-check">
                  <input
                    type="checkbox"
                    class="form-check-input"
                    id="addBookRead"
                    v-model="addBookForm.read"
                  />
                  <label class="form-check-label" for="addBookRead">Read</label>
                </div>
              </div>
            </form>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" @click="handleAddReset">Reset</button>
            <button type="button" class="btn btn-primary" @click="handleAddSubmit">Add</button>
          </div>
        </div>
      </div>
    </div>

    <!-- edit book modal -->
    <div
      ref="editBookModal"
      class="modal fade"
      :class="{ show: activeEditBookModal, 'd-block': activeEditBookModal }"
      tabindex="-1"
      role="dialog"
    >
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Edit Book</h5>
            <button type="button" class="close" @click="toggleEditBookModal(null)">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <form>
              <div class="form-group">
                <label for="editBookTitle">Title</label>
                <input
                  type="text"
                  class="form-control"
                  id="editBookTitle"
                  v-model="editBookForm.title"
                />
              </div>
              <div class="form-group">
                <label for="editBookAuthor">Author</label>
                <input
                  type="text"
                  class="form-control"
                  id="editBookAuthor"
                  v-model="editBookForm.author"
                />
              </div>
              <div class="form-group">
                <div class="form-check">
                  <input
                    type="checkbox"
                    class="form-check-input"
                    id="editBookRead"
                    v-model="editBookForm.read"
                  />
                  <label class="form-check-label" for="editBookRead">Read</label>
                </div>
              </div>
            </form>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" @click="handleEditCancel">Cancel</button>
            <button type="button" class="btn btn-primary" @click="handleEditSubmit">Update</button>
          </div>
        </div>
      </div>
    </div>

    <!-- Delete Confirmation Modal -->
    <div
      ref="deleteConfirmationModal"
      class="modal fade"
      :class="{ show: showDeleteConfirmationModal, 'd-block': showDeleteConfirmationModal }"
      tabindex="-1"
      role="dialog"
    >
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Delete Confirmation</h5>
            <button type="button" class="close" @click="showDeleteConfirmationModal = false">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <p>Are you sure you want to delete this book?</p>
          </div>
          <div class="modal-footer">
            <button
              type="button"
              class="btn btn-secondary"
              @click="handleDeleteCancel"
            >
              Cancel
            </button>
            <button type="button" class="btn btn-danger" @click="handleDeleteConfirmation">Delete</button>
          </div>
        </div>
      </div>
    </div>

   
    <div
      v-if="activeAddBookModal || activeEditBookModal || showDeleteConfirmationModal"
      class="modal-backdrop fade show"
    ></div>
    <div class="pagination">
      <button class="btn btn-primary" @click="previousPage" :disabled="currentPage === 1">
        Previous
      </button>
      <button
        v-for="pageNumber in totalPages"
        :key="pageNumber"
        class="btn btn-primary"
        @click="goToPage(pageNumber)"
        :disabled="pageNumber === currentPage"
      >
        {{ pageNumber }}
      </button>
      <button class="btn btn-primary" @click="nextPage" :disabled="currentPage === totalPages">
        Next
      </button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import AlertPath from './AlertPath.vue';

export default {
  data() {
    return {
      activeAddBookModal: false,
      activeEditBookModal: false,
      showDeleteConfirmationModal: false,
      addBookForm: {
        title: '',
        author: '',
        read: [],
        titleTouched: false,
        authorTouched: false,
      },
      editBookForm: {
        id: '',
        title: '',
        author: '',
        read: [],
      },
      deleteBook: null,
      books: [],
      message: '',
      showMessage: false,
      currentPage: 1,
      pageSize: 10,
    };
  },
  components: {
    AlertPath,
  },
  computed: {
    paginatedBooks() {
      const startIndex = (this.currentPage - 1) * this.pageSize;
      const endIndex = startIndex + this.pageSize;
      return this.books.slice(startIndex, endIndex);
    },
    totalPages() {
      return Math.ceil(this.books.length / this.pageSize);
    },
  },
  methods: {
    addBook(payload) {
      const path = 'http://localhost:5000/books';
      axios
        .post(path, payload)
        .then(() => {
          this.getBooks();
          this.message = 'Book added!';
          this.showMessage = true;
          this.toggleAddBookModal();
        })
        .catch((error) => {
          console.error(error);
          this.getBooks();
        });
    },
    getBooks() {
      const startIndex = (this.currentPage - 1) * this.pageSize;
      const endIndex = startIndex + this.pageSize;
      const path = `http://localhost:5000/books?startIndex=${startIndex}&endIndex=${endIndex}`;

      axios
        .get(path)
        .then((res) => {
          this.books = res.data.books;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    handleAddReset() {
      this.initForm();
      this.$router.push('/books/addbook');
    },
    handleAddSubmit() {
      this.addBookForm.titleTouched = true;
      this.addBookForm.authorTouched = true;

      if (!this.addBookForm.title || !this.addBookForm.author) {
        return; 
      }
      let read = false;
      if (this.addBookForm.read[0]) {
        read = true;
      }
      const payload = {
        title: this.addBookForm.title,
        author: this.addBookForm.author,
        read, 
      };
      this.addBook(payload);
      this.initForm();
      this.$router.push('/books/addbook/add');
    },
       handleEditSubmit() {
      this.toggleEditBookModal(null);
      if (!this.editBookForm.title || !this.editBookForm.author) {
        return; 
      }
      let read = false;
      if (this.editBookForm.read[0]) {
        read = true;
      }
      const payload = {
        title: this.editBookForm.title,
        author: this.editBookForm.author,
        read, 
      };
      this.updateBook(payload, this.editBookForm.id);
      this.$router.push('/books/addbook/updated');

    },
    handleEditCancel() {
      this.toggleEditBookModal(null);
      this.initForm();
      this.$router.push('/books/list');

    },
    handleDeleteBook(book) {
      this.deleteBook = book;
      this.showDeleteConfirmationModal = true;
    },
    handleDeleteConfirmation() {
      this.showDeleteConfirmationModal = false;
      const bookID = this.deleteBook.id;
      this.removeBook(bookID);
    },
    handleDeleteCancel() {
      this.showDeleteConfirmationModal = false;
      this.$router.push('/books/list');
    },
    removeBook(bookID) {
      const path = `http://localhost:5000/books/${bookID}`;
      axios
        .delete(path)
        .then(() => {
          this.getBooks();
          this.message = 'Book removed!';
          this.showMessage = true;
        })
        .catch((error) => {
          console.error(error);
          this.getBooks();
        });
    },
    initForm() {
      this.addBookForm.title = '';
      this.addBookForm.author = '';
      this.addBookForm.read = [];
      this.editBookForm.id = '';
      this.editBookForm.title = '';
      this.editBookForm.author = '';
      this.editBookForm.read = [];
    },
    toggleAddBookModal() {
      const body = document.querySelector('body');
      this.activeAddBookModal = !this.activeAddBookModal;
      if (this.activeAddBookModal) {
        body.classList.add('modal-open');
      } else {
        body.classList.remove('modal-open');
      }
    },
    toggleEditBookModal(book) {
      if (book) {
        this.editBookForm = book;
      }
      const body = document.querySelector('body');
      this.activeEditBookModal = !this.activeEditBookModal;
      if (this.activeEditBookModal) {
        body.classList.add('modal-open');
      } else {
        body.classList.remove('modal-open');
      }
    },
    updateBook(payload, bookID) {
      const path = `http://localhost:5000/books/${bookID}`;
      axios
        .put(path, payload)
        .then(() => {
          this.getBooks();
          this.message = 'Book updated!';
          this.showMessage = true;
        })
        .catch((error) => {
          console.error(error);
          this.getBooks();
        });
    },
    nextPage() {
      if (this.currentPage < this.totalPages) {
        this.currentPage++;
        this.getBooks();
      }
    },
    previousPage() {
      if (this.currentPage > 1) {
        this.currentPage--;
        this.getBooks();
      }
    },
    goToPage(pageNumber) {
      this.currentPage = pageNumber;
      this.getBooks();
    },
  },
  created() {
    this.getBooks();
  },
};
</script>



<style scoped>
.modal.show {
  display: block;
  background: rgba(0, 0, 0, 0, 0, 0.5);
}
.modal.fade.show {
  opacity: 1;
}
.text-danger {
  color: red;
}
.pagination {
  margin-top: 20px;
  display: flex;
  justify-content: center;
}
.pagination button {
  margin-right: 5px;
}
</style>
