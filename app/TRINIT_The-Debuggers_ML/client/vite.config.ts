import { defineConfig, loadEnv } from "vite";
import { port } from "./src/config";
import react from "@vitejs/plugin-react";
import { fileURLToPath } from "url";

// https://vitejs.dev/config/
export default ({ mode }) => {
	const env = loadEnv(mode, process.cwd(), "");
	return defineConfig({
	  define: {
		"process.env": env,
	  },
	  plugins: [react()],
	  server: {
		port: port,
	  },
	  resolve: {
		alias: {
		  "@": fileURLToPath(new URL("./src", import.meta.url)),
		},
	  },
	});
  };