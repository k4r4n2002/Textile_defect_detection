import { CameraComponent } from "../../components";
import styles from "./styles.module.css";

const Home = (): JSX.Element => {
	return (
		<>
			<div className={styles.section} >
				<h1 className={styles.header}>Automated Road Damage Detection for Infrastructure Maintenance</h1>
				<h2 className={styles.subheader}>(By The Debuggers Team)</h2>
				
				<div className={styles.camera}>
					<CameraComponent />
				</div>
			</div>
		</>
	);
};

export default Home;