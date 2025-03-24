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
            posts = data.posts;
        });
    }
</script>
  
<main class="container mx-auto p-4">
    <h1 class="text-3xl font-bold mb-4">Posts</h1>
    
    {#if $user != null}
    <div class="mb-6">
      <div class="flex items-center space-x-2">
        <input
          type="text"
          placeholder="New post title"
          bind:value={newPostTitle}
          class="border border-gray-300 rounded p-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
        <input
          type="text"
          placeholder="New post content"
          bind:value={newPostContent}
          class="border border-gray-300 rounded p-2 focus:outline-none focus:ring-2 focus:ring-blue-500 flex-grow"
        />
        <button
          on:click={addPost}
          class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
        >
          Submit
        </button>
      </div>
    </div>
    {/if}

    {#if posts.length === 0}
    <p class="text-gray-500">Loading posts...</p>
  {:else}
    <div class="space-y-6">
      {#each posts as post}
        <div class="w-full bg-white border border-gray-200 rounded-lg shadow hover:shadow-lg transition duration-300 dark:bg-gray-800 dark:border-gray-700">
          <div class="p-5">
            <h2 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">{post.title}</h2>
            <p class="mb-3 font-normal text-gray-700 dark:text-gray-400">{post.content}</p>
            <p class="text-sm text-gray-500">Author: {post.author}</p>

            {#if $user != null}
            <div class="mt-4 flex items-center space-x-2">
              <input
                type="text"
                placeholder="Add a comment"
                bind:value={newComments[post.post_id]}
                class="border border-gray-300 rounded p-2 focus:outline-none focus:ring-2 focus:ring-green-500 flex-grow"
              />
              <button
                on:click={() => addComment(post.post_id)}
                class="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded"
              >
                Comment
              </button>
            </div>
            {/if}

            {#if post.comments && post.comments.length > 0}
              <div class="mt-4 border-t border-gray-200 pt-4">
                <h3 class="text-xl font-semibold mb-2">Comments</h3>
                <ul class="space-y-4">
                  {#each post.comments as comment}
                    <li class="bg-gray-50 p-3 rounded-lg dark:bg-gray-700">
                      <p class="text-gray-700 dark:text-gray-300">{comment.content}</p>
                      <p class="text-xs text-gray-500">- {comment.author}</p>
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
  