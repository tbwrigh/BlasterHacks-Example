<script>
	import '../app.css';
	let { children } = $props();
	import { Navbar, NavBrand, NavUl, NavLi } from 'flowbite-svelte';
	import { user } from '../stores/auth';

	const logout = () => {
		user.set(null);
		window.location.href = '/';
	};
</script>

<div class="flex flex-col min-h-screen">
	<header class="flex-none">
		<Navbar class="h-16">
			<NavBrand href="/">
				<img src="/logo.svg" class="mr-3 h-6 sm:h-9" alt="Logo" />
				<span class="self-center whitespace-nowrap text-xl font-semibold">My App</span>
			</NavBrand>
			<NavUl>
				<NavLi href="/">Home</NavLi>
				{#if $user != null}
					<NavLi on:click={logout} href="/">Logout</NavLi>
				{:else}
					<NavLi href="/login">Login</NavLi>
				{/if}
			</NavUl>
		</Navbar>
	</header>

	<div class="flex flex-col flex-1">
		<main class="flex-1 container mx-auto h-full">
			{@render children()}
		</main>

		<footer class="flex-none bg-gray-200 py-6">
			<div class="container mx-auto text-center text-gray-600">
				© {new Date().getFullYear()} My App. All rights reserved.
			</div>
		</footer>
	</div>
</div>
