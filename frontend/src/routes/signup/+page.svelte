<script lang="ts">
	let email = '';
	let password = '';
    let username = '';

    import { user } from '../../stores/auth';
    import { goto } from '$app/navigation';

    if ($user) {
        goto('/');
    }

	const handleSubmit = () => {
        fetch('http://localhost:8000/user/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify
            ({
                email: email,
                password: password,
                username: username
            })
        })
        .then((response) => {
            if (response.ok) {
                return response.json();
            } else {
                return { error: true, message: 'An error occurred. Please try again.' };
            }
        }).then((data) => {
            if (data.error) {
                alert(data.message);
            } else {
                goto('/login');
            }
        });
        
	};
</script>

<div class="h-full flex items-center justify-center">
	<div class="w-full max-w-md bg-white rounded-lg shadow-md p-8 border border-gray-200">
		<h2 class="text-2xl font-semibold text-center mb-6">Sign Up</h2>
		<form on:submit|preventDefault={handleSubmit} class="space-y-6">
			<div>
				<label class="block text-sm font-medium text-gray-700">Email</label>
				<input
					type="email"
					bind:value={email}
					required
					class="mt-1 block w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
				/>
			</div>
            <div>
				<label class="block text-sm font-medium text-gray-700">Username</label>
				<input
					type="text"
					bind:value={username}
					required
					class="mt-1 block w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
				/>
			</div>
			<div>
				<label class="block text-sm font-medium text-gray-700">Password</label>
				<input
					type="password"
					bind:value={password}
					required
					class="mt-1 block w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
				/>
			</div>
			<button
				type="submit"
				class="w-full bg-blue-500 text-white py-2 px-4 rounded-md hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2"
			>
				Login
			</button>
		</form>
		<p class="text-sm text-gray-600 mt-6 text-center">
			Already have an account?
			<a href="/login" class="text-blue-500 hover:underline">Login</a>
		</p>
	</div>
</div>
