import time
import shutil


def format_time(seconds):
    m, s = divmod(seconds, 60)
    return f"{int(m):02d}:{int(s):02d}"


def ft_tqdm(lst: range) -> None:
    total = len(lst)
    start_time = time.time()

    terminal_width = shutil.get_terminal_size().columns - 30
    progress_bar_width = terminal_width - 10

    for i, item in enumerate(lst, start=1):
        progress = int(i / total * progress_bar_width)
        print(progress)
        elapsed_time = time.time() - start_time
        print(elapsed_time)
        speed = i / elapsed_time
        print(speed)
        eta = (total - i) / speed
        print(eta)

        elapsed_formatted = format_time(elapsed_time)
        print(elapsed_formatted)
        eta_formatted = format_time(eta)
        print(eta_formatted)

        progress_bar = f"|{'█' * progress:<{progress_bar_width}}|"
        progress_percentage = progress * 100 // progress_bar_width
        progress_info = f"{progress_percentage}%{progress_bar} {i}/{total}"
        time_info = f"[{elapsed_formatted}<{eta_formatted}, {speed:.2f}it/s]"

        print(f"\r{progress_info} {time_info}", end="", flush=True)
        yield item


def main():
    for _ in ft_tqdm(range(0, 333)):
        pass


if __name__ == "__main__":
    main()