<script>
    import { goto } from '$app/navigation';
    import { user } from '../stores/auth';

    import { onMount } from 'svelte';

    let posts = [];

    onMount(() => {
        getPosts();
    });

    let newPostTitle = "";
    let newPostContent = "";
    let newComments = {};

    function addPost() {
        fetch('http://localhost:8000/post/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${$user}`
            },
            body: JSON.stringify({
                title: newPostTitle,
                content: newPostContent
            })
        })
        .then((response) => response.json())
        .then((data) => {
            console.log(data)
            getPosts();
            newPostContent = "";
            newPostTitle = "";
        });
    }

    function addComment(id) {
        fetch(`http://localhost:8000/post/comment`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${$user}`
            },
            body: JSON.stringify({
                post_id: id,
                content: newComments[id]
            })
        })
        .then((response) => response.json())
        .then((data) => {
            console.log(data)
            getPosts();
            newComments[id] = "";
        });
    }

    function getPosts() {
        fetch('http://localhost:8000/post/', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            }
        })
        .then((response) => response.json())
        .then((data) => {
            console.log(data)
            posts = data.posts;
        });
    }
</script>
  
<main class="container mx-auto p-4">  <!-- Main container with Flowbite/Tailwind styling for layout 🏠✨ -->
    <h1 class="text-3xl font-bold mb-4">Posts</h1>  <!-- Posts header styled with large, bold text 📢💡 -->
    
    {#if $user != null}
    <div class="mb-6">  <!-- Form container placed under the header with bottom margin for spacing 🗂️🔧 -->
      <div class="flex items-center space-x-2">  <!-- Flex container for inputs and button in a single row 😊📏 -->
        <input
          type="text"
          placeholder="New post title"
          bind:value={newPostTitle}
          class="border border-gray-300 rounded p-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
        />  <!-- Title input with fixed width styling ✏️✨ -->
        <input
          type="text"
          placeholder="New post content"
          bind:value={newPostContent}
          class="border border-gray-300 rounded p-2 focus:outline-none focus:ring-2 focus:ring-blue-500 flex-grow"
        />  <!-- Content input set to flex-grow to fill available space between title and button 💭📏 -->
        <button
          on:click={addPost}
          class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
        >
          Submit
        </button>  <!-- Submit button with blue styling and hover effect for interactivity 🔘🚀 -->
      </div>
    </div>
    {/if}

    {#if posts.length === 0}
    <p class="text-gray-500">Loading posts...</p>  <!-- Loading message while posts are being fetched ⏳🔄 -->
  {:else}
    <div class="space-y-6">  <!-- Vertical spacing between full-width post cards for clear separation 🗂️📊 -->
      {#each posts as post}
        <div class="w-full bg-white border border-gray-200 rounded-lg shadow hover:shadow-lg transition duration-300 dark:bg-gray-800 dark:border-gray-700">  <!-- Full-width post card styled with Flowbite/Tailwind classes 🎴✨ -->
          <div class="p-5">
            <h2 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">{post.title}</h2>  <!-- Render the post title with prominent styling 📰💫 -->
            <p class="mb-3 font-normal text-gray-700 dark:text-gray-400">{post.content}</p>  <!-- Render the post content styled for readability 🗒️🖊️ -->
            <p class="text-sm text-gray-500">Author: {post.author}</p>  <!-- Display the post author with smaller, subtle text styling 👤📌 -->

            {#if $user != null}
            <div class="mt-4 flex items-center space-x-2">  <!-- Container for comment input and button in a row 💬📏 -->
              <input
                type="text"
                placeholder="Add a comment"
                bind:value={newComments[post.post_id]}
                class="border border-gray-300 rounded p-2 focus:outline-none focus:ring-2 focus:ring-green-500 flex-grow"
              />  <!-- Comment input box that grows to fill available space ✍️✨ -->
              <button
                on:click={() => addComment(post.post_id)}
                class="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded"
              >
                Comment
              </button>  <!-- Comment button styled with green for a fresh look 💚🚀 -->
            </div>
            {/if}

            {#if post.comments && post.comments.length > 0}  <!-- Conditionally render the comments section if comments exist for the post 💬✅ -->
              <div class="mt-4 border-t border-gray-200 pt-4">  <!-- Comments section with top border for visual separation 🧱📏 -->
                <h3 class="text-xl font-semibold mb-2">Comments</h3>  <!-- Comments header styled with bold text 📢📝 -->
                <ul class="space-y-4">
                  {#each post.comments as comment}
                    <li class="bg-gray-50 p-3 rounded-lg dark:bg-gray-700">  <!-- Individual comment styled with a light background and padding for clarity 🌟🗒️ -->
                      <p class="text-gray-700 dark:text-gray-300">{comment.content}</p>  <!-- Render the comment content in a readable format 💭✨ -->
                      <p class="text-xs text-gray-500">- {comment.author}</p>  <!-- Display the comment author in a smaller, subtle font 👤🖋️ -->
                    </li>
                  {/each}
                </ul>
              </div>
            {/if}
          </div>
        </div>
      {/each}
    </div>
  {/if}
  </main>
  