import importlib
from typing import Any


def check_deps() -> tuple[dict[str, Any], bool]:
    try:
        dependecies = [('pandas', 'Data Manipulation'),
                       ('numpy', 'Numerical Computation'),
                       ('requests', 'Network accesss'),
                       ('matplotlib', 'Visualization')]
        modules = {}
        all_ok = True
        for dep, dep_type in dependecies:
            try:
                module = importlib.import_module(dep)
                version = module.__version__
                print(f"[OK] {dep} ({version}) - {dep_type} ready")
                modules[dep] = module
            except Exception:
                if dep == "requests":
                    print(f"[OPTIONAL] {dep} not found")
                    continue
                all_ok = False
                print(f"[MISSING] {dep} - {dep_type} not found \n"
                      f"       -> Install with pip: pip install {dep}\n"
                      f"       -> Or with poetry: poetry add {dep}")
        if not all_ok:
            print("\nInstall all dependecies with the pip command: "
                  "pip install -r requirements.txt\n"
                  "Or with the poetry command: "
                  "poetry install -> poetry run python3 loading.py\n"
                  "\nERROR: Missing required dependecies. Aborting.\n")
            return ({}, all_ok)
        return (modules, all_ok)
    except Exception as e:
        print(f"Error on check_deps(): {e}")
        return ({}, False)


def analyze_matrix(modules: dict[str, Any]) -> None:
    try:
        pandas = modules["pandas"]
        numpy = modules["numpy"]
        position = numpy.random.rand(1000)
        time = numpy.arange(1000)
        data_f = pandas.DataFrame({"time": time, "position": position})
        print("\nAnalyzing Matrix data...\n"
              "Processing 1000 data points...\n"
              "Generating visualization...\n\n")
        generate_visualization(data_f)
    except Exception as e:
        print(f"Error on analyze_matrix(): {e}")


def generate_visualization(data_f: Any) -> None:
    try:
        import matplotlib.pyplot as plot
        file_name = "matrix_analysis.png"
        plot.figure(figsize=(20, 10))
        plot.plot(data_f["time"], data_f["position"])
        plot.title("Matrix Position-Time Analysis")
        plot.xlabel("Time")
        plot.ylabel("Position")
        plot.grid(True)
        plot.savefig(file_name)
        plot.close()
        print("Analysis complete!\n"
              f"Results saved to: {file_name}")
    except Exception as e:
        print(f"Error on generate_visualization(): {e}")


def loading() -> None:
    print("\nLOADING STATUS: Loading programs...\n"
          "Checking dependencies:\n")
    modules, all_ok = check_deps()
    if all_ok:
        analyze_matrix(modules)


if __name__ == '__main__':
    loading()
