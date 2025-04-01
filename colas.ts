
class Video {
    constructor(public title: string, public duration: number) {} 
}
class Queue<T> {
    private items: T[] = [];

    enqueue(item: T): void {
        this.items.push(item);
    }

    dequeue(): T | undefined {
        return this.items.shift(); 
    }

    isEmpty(): boolean {
        return this.items.length === 0;
    }

    size(): number {
        return this.items.length;
    }

    peek(): T | undefined {
        return this.items[0]; 
    }
}
class VideoPlayer {
    private playlist: Queue<Video> = new Queue();

    addVideo(video: Video): void {
        console.log(`Agregado: ${video.title} (${video.duration}s)`);
        this.playlist.enqueue(video);
    }

    playNext(): void {
        if (this.playlist.isEmpty()) {
            console.log("No hay más videos en la lista.");
            return;
        }

        const video = this.playlist.dequeue();
        console.log(`Reproduciendo: ${video?.title} (${video?.duration}s)`);
    }

    showNextVideo(): void {
        const nextVideo = this.playlist.peek();
        if (nextVideo) {
            console.log(`Siguiente video: ${nextVideo.title}`);
        } else {
            console.log("No hay más videos en la lista.");
        }
    }
}

const player = new VideoPlayer();


player.addVideo(new Video("Intro a TypeScript", 300));
player.addVideo(new Video("Avanzando en TypeScript", 450));
player.addVideo(new Video("Proyectos con TypeScript", 600));


player.showNextVideo();


player.playNext();
player.playNext();
player.playNext();
player.playNext(); 
