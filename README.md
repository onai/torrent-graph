Graph analysis of torrents
Graph analysis on real torrent network, with sample results for data from the movie Sintel.

# Table Of Contents
1. [Background](#Background)
2. [Sample results](#sample-results)
3. [How To Run](#how-to-run)
4. [References](#References)

# Background
Bittorrent networks can find peers to download a torrent from using either Bittorrent trackers or Bittorrent DHT (Distributed Hash Table). In Bittorrent DHT terminology, a "peer" is a client/server listening on a TCP port that implements the BitTorrent protocol. A "node" is a client/server listening on a UDP port implementing the distributed hash table protocol. The DHT is composed of nodes and stores the location of peers. BitTorrent clients include a DHT node, which is used to contact other nodes in the DHT to get the location of peers to download from using the BitTorrent protocol [1]
Trackers are central servers that can introduce a client to another client that has a particular piece of a torrent. Bittorrent DHTs (“trackerless” servers) are decentralized client/servers that anyone can host instead of depending on the tracker. Bittorrent DHTs is based on Kademlia protocol [2]. The Bittorrent protocol with DHT is not totally decentralized because the network still requires bootstrap servers to direct the client towards the most likely node that has the desired piece.
A file that is shared using Bittorrent is divided into equally-sized pieces and shared among those clients who request the pieces [3]. Each piece is assigned an infohash, which is just a SHA [4] hash of the piece.

Figure 1: Graph of a crawl for infohash 08ada5a7a6183aae1e09d831df6748d566095a10

# Sample results
In the experiment we describe here, we analyzed the structure of the bittorrent DHT graph of one piece (with infohash 08ada5a7a6183aae1e09d831df6748d566095a10) of the torrent of the movie Sintel [5], which is under the Creative Commons Attribution 3.0 license [6]. We started the crawl by sending a get_peers request to a list of bootstrap servers. Bootstrap servers respond with a list of nodes which might have that particular piece. The next step was to iteratively go through the list of nodes and send them a get_peers request. The nodes would either respond with a list of peers, which had the piece requested, or with a list of nodes that are closest to the infohash of the piece supplied in the query. If the nodes responded with a list of other nodes, we iterated through the list of new nodes and sent a get_peers request and repeated the process. The graph obtained from this process is displayed in Fig. 1. 
Using the graph obtained from the last step, we found nodes that formed the centers of large clusters using PageRank. We found that the top 3 nodes—102.176.200.130:6881, 151.237.18.23:51413, 109.201.133.134:20027—with pageranks 0.06489, 0.0065, and 0.0051, respectively, are the nodes in the center of the biggest clusters in the network. 102.176.200.130:6881 is the center of bottom-right cluster in Fig. 1.
The bittorrent network is incredibly large and clients that run the protocol span across the globe. With the above framework, we could crawl the nodes of bittorrent network that support the DHT protocol. Given a torrent or a magnet link, we can crawl for all pieces of the torrent and then construct and conduct meaningful analysis of the graph.
# How To Run
1. Install requirements by running `pip install requirements.txt`
2. Clone https://github.com/Trrnts/Trrnts and follow install instructions for Redis and Node
            `git clone https://github.com/Trrnts/Trrnts.git`
3. Start Redis server with command `redis-server`
4. Patch `crawl.js` by running `git apply --reject --whitespace=fix crawl.patch`
5. Start node server with `node server`
6. Start the crawl by running `node workers/masterCrawler`
7. Go to `http://localhost:9000` and click on `Submit a magnet`
8. Paste this magnet link into the url:
``` magnet:?xt=urn:btih:08ada5a7a6183aae1e09d831df6748d566095a10&dn=Sintel&tr=udp%3A%2F%2Fexplodie.org%3A6969&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969&tr=udp%3A%2F%2Ftracker.empire-js.us%3A1337&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337&tr=wss%3A%2F%2Ftracker.btorrent.xyz&tr=wss%3A%2F%2Ftracker.fastcast.nz&tr=wss%3A%2F%2Ftracker.openwebtorrent.com&ws=https%3A%2F%2Fwebtorrent.io%2Ftorrents%2F&xs=https%3A%2F%2Fwebtorrent.io%2Ftorrents%2Fsintel.torrent
```
9. Then the crawler starts printing nodes onto the shell
10. Format the data into a dictionary as in `data_file.py`
11. To visualize, run `python plot.py`

# References
[1]: http://www.bittorrent.org/beps/bep_0005.html
[2]: Peter Maymounkov, David Mazieres, "Kademlia: A Peer-to-peer Information System Based on the XOR Metric", IPTPS 2002. http://www.cs.rice.edu/Conferences/IPTPS02/109.pdf
[3]: http://mg8.org/processing/bt.html
[4]: Secure Hash Standard - SHS: Federal Information Processing Standards Publication 180-4. NIST, U.S. Department of Commerce. 2012. 
[5]: Creative Commons Attribution 3.0 license
[6]: https://www.imdb.com/title/tt1727587/
