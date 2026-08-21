import sys
from urllib.parse import urlparse, parse_qs
import yt_dlp
from rich.console import Console
from rich.panel import Panel

console = Console()


def is_single_video_url(url):
    """A bare playlist URL has 'list' but no 'v' — reject those outright."""
    parsed = urlparse(url)
    query = parse_qs(parsed.query)
    if 'list' in query and 'v' not in query:
        return False
    return True


def download_video(url):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'noplaylist': True,
    }
    try:
        console.print("\n[bold cyan]⏳ Fetching video information and starting download...[/bold cyan]")

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        console.print(Panel("[bold green]✅ Download completed successfully![/bold green]", border_style="green"))

    except yt_dlp.utils.DownloadError:
        console.print("[bold red]❌ Error: Invalid URL or video is unavailable.[/bold red]")
    except Exception as e:
        console.print(f"[bold red]❌ An unexpected error occurred: {e}[/bold red]")


def main():
    console.print(Panel("[bold magenta]🎥 YouTube Video Downloader[/bold magenta]", expand=False))

    if len(sys.argv) > 1:
        url = sys.argv[1].strip()
    else:
        url = console.input("[bold green]Enter the YouTube Video URL: [/bold green]").strip()

    if not url.startswith("http") or ("youtube.com" not in url and "youtu.be" not in url):
        console.print("[bold red]❌ Error: Please enter a valid YouTube URL (e.g., https://www.youtube.com/... or https://youtu.be/...)[/bold red]")
        return

    if not is_single_video_url(url):
        console.print("[bold red]❌ Error: This looks like a playlist link. This tool only downloads a single video — paste a link to one specific video instead.[/bold red]")
        return

    download_video(url)


if __name__ == "__main__":
    main()