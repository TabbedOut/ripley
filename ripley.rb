require 'json'
require 'yaml'


def format_geojson_from_docs(docs)
    out = {
        type: 'FeatureCollections',
        features: [],
    }
    docs.each {|doc|
        coordinates = doc.delete('coordinates')
        if coordinates
            out[:features].push({
                type: 'Feature',
                properties: doc,
                geometry: {
                    type: 'Point',
                    coordinates: coordinates.split(', ').reverse,
                },
            })
        end
        }
    out
end


docs = YAML.load_documents(File.open('suchnoms.yml'))
puts format_geojson_from_docs(docs).to_json
