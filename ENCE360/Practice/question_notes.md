# Definitions

### Caching

- Write-through: Always write to disk
- Write-back: write to disk only when evicting (even when unchanged)
- Write-deferred: mark cache entry as `dirty` if changed, write out dirty entry on eviction
- Write-allocation: bring missed entry into cache

**Problem with direct cache mapping**

That every single address in memory can only ever exist at one location within the cache, this is a problem if you want to have two distinct memory addresses that want to map to the same cache address, *constant evicting to read another one in (inefficient).*

Associative and set Associative caching gets around this by allowing memory addresses to be mapped to multiple locations in the cache.

> This addressable memory is more expensive and requires more space in order to hold the tag.



